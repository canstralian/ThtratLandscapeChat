import gradio as gr
import tempfile


# ---------------------------------------------------------------------------
# Backend logic per mode (stub functions to plug your real engine into)
# ---------------------------------------------------------------------------


def handle_threat_intel(message, files):
    out = f"[Threat Intel] Processed: {message}"
    if files:
        out += f" | Files: {[f.name for f in files]}"
    return out


def handle_translation(message, files):
    out = f"[Translation] Interpreted: {message}"
    if files:
        out += " | (Files attached for context)"
    return out


def handle_marketplace_watch(message, files):
    out = f"[Marketplace Watch] Monitoring request: {message}"
    return out


def handle_analyst_tools(message, files):
    out = f"[Analyst Tools] Action: {message}"
    return out


MODE_ROUTER = {
    "Threat Intel": handle_threat_intel,
    "Translation": handle_translation,
    "Marketplace Watch": handle_marketplace_watch,
    "Analyst Tools": handle_analyst_tools,
}

# ---------------------------------------------------------------------------
# Core message processing
# ---------------------------------------------------------------------------


def process_message(message, files, history, mode):
    if not message and not files:
        return history, history  # no-op

    handler = MODE_ROUTER.get(mode, handle_threat_intel)
    response = handler(message or "(no text, files only)", files)

    user_label = f"{mode}: {message or '[files only]'}"
    history = history + [(user_label, response)]

    # Clear text input on submit handled by UI (by setting value="")
    return history, history


def clear_chat():
    return [], []


def download_chat(history):
    # Convert chat history to a text file and return its path
    if not history:
        content = "No conversation yet.\n"
    else:
        lines = []
        for user_msg, bot_msg in history:
            lines.append(f"[User]: {user_msg}")
            lines.append(f"[System]: {bot_msg}")
            lines.append("")  # blank line between turns
        content = "\n".join(lines)

    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".txt")
    with open(tmp_file.name, "w", encoding="utf-8") as f:
        f.write(content)

    return tmp_file.name


# ---------------------------------------------------------------------------
# Mobile-first UI
# ---------------------------------------------------------------------------

with gr.Blocks(title="Mobile-First Intelligence Console") as demo:

    gr.Markdown("## 🛰 Intelligence Console")

    # Global chat state
    chat_state = gr.State([])

    # Mode selector at top (full width)
    mode = gr.Radio(
        ["Threat Intel", "Translation", "Marketplace Watch", "Analyst Tools"],
        value="Threat Intel",
        label="Mode",
        interactive=True
    )

    # Chat area (full-width, tall enough but scrollable on mobile)
    chat = gr.Chatbot(
        label="Dialogue",
        height=430,
        show_copy_button=True
    )

    # Utility + attachments collapsed on mobile to reduce clutter
    with gr.Accordion("Attachments & Utilities", open=False):
        file_input = gr.File(
            label="Upload files (logs, screenshots, docs)",
            file_count="multiple"
        )
        with gr.Row(variant="compact"):
            clear_btn = gr.Button("Clear Chat", variant="secondary")
            download_btn = gr.Button("Download Transcript", variant="secondary")
        download_file = gr.File(
            label="Transcript File",
            interactive=False
        )

    # Input bar at bottom: textbox + send button in a compact row
    with gr.Row(variant="compact"):
        user_input = gr.Textbox(
            placeholder="Type your message...",
            label="",
            scale=5
        )
        send_btn = gr.Button("Send", variant="primary", scale=1)

    # -----------------------------------------------------------------------
    # Event wiring
    # -----------------------------------------------------------------------

    # Send via button
    send_btn.click(
        fn=process_message,
        inputs=[user_input, file_input, chat_state, mode],
        outputs=[chat, chat_state]
    ).then(
        lambda: "",
        inputs=None,
        outputs=user_input  # clear input after send
    )

    # Send via Enter key
    user_input.submit(
        fn=process_message,
        inputs=[user_input, file_input, chat_state, mode],
        outputs=[chat, chat_state]
    ).then(
        lambda: "",
        inputs=None,
        outputs=user_input
    )

    # Clear chat
    clear_btn.click(
        fn=clear_chat,
        inputs=None,
        outputs=[chat, chat_state]
    )

    # Download transcript
    download_btn.click(
        fn=download_chat,
        inputs=chat_state,
        outputs=download_file
    )

demo.launch()
