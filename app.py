import streamlit as st
from openai import OpenAI
import base64

st.set_page_config(
    page_title="ChatX",
    page_icon="💬",
    layout="wide"
)

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ---------- CSS ----------
st.markdown("""
<style>
[data-testid="stSidebar"] {
    background-color: #171717;
}
[data-testid="stSidebar"] * {
    color: white;
}
.block-container {
    padding-top: 2rem;
    max-width: 900px;
}
.chat-title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    margin-top: 40px;
}
.chat-subtitle {
    text-align: center;
    color: #8e8e8e;
    margin-bottom: 40px;
}
.stChatInput {
    max-width: 850px;
    margin: auto;
}
</style>
""", unsafe_allow_html=True)

# ---------- Session State ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "memory" not in st.session_state:
    st.session_state.memory = ""

# ---------- Sidebar ----------
with st.sidebar:
    st.title("💬 ChatX")

    if st.button("➕ New Chat", use_container_width=True):
        if st.session_state.messages:
            first_msg = st.session_state.messages[0]["content"][:35]
            st.session_state.chat_history.append(first_msg)
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.caption("Chats")

    if st.session_state.chat_history:
        for chat in st.session_state.chat_history[::-1]:
            st.button(chat, use_container_width=True)
    else:
        st.caption("No previous chats")

    st.markdown("---")

    model = st.selectbox(
        "Model",
        ["gpt-4o-mini", "gpt-4o"]
    )

    st.markdown("---")

    st.subheader("Memory")
    st.session_state.memory = st.text_area(
        "What should ChatX remember?",
        value=st.session_state.memory,
        placeholder="Example: I am a CS & Business student at Concordia.",
        height=100
    )

    st.markdown("---")

    uploaded_file = st.file_uploader(
        "Upload file",
        type=["txt", "md", "py", "csv", "json", "html", "css", "js"]
    )

    uploaded_image = st.file_uploader(
        "Upload image",
        type=["png", "jpg", "jpeg"],
        key="image_upload"
    )

    st.markdown("---")
    st.caption("Built by ChatX")

# ---------- Home Screen ----------
if not st.session_state.messages:
    st.markdown("<div class='chat-title'>What can I help with?</div>", unsafe_allow_html=True)
    st.markdown("<div class='chat-subtitle'>ChatX can answer questions, write code, analyze files, and help you build.</div>", unsafe_allow_html=True)

# ---------- Show Messages ----------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------- File Context ----------
file_context = ""

if uploaded_file is not None:
    try:
        file_context = uploaded_file.read().decode("utf-8")
        st.sidebar.success("File uploaded")
    except Exception:
        st.sidebar.error("Could not read file")

# ---------- Image Context ----------
image_content = None

if uploaded_image is not None:
    image_bytes = uploaded_image.read()
    image_base64 = base64.b64encode(image_bytes).decode("utf-8")

    image_content = {
        "type": "image_url",
        "image_url": {
            "url": f"data:image/jpeg;base64,{image_base64}"
        }
    }

    st.sidebar.image(uploaded_image, caption="Uploaded image")

# ---------- Chat ----------
user_input = st.chat_input("Message ChatX...")

if user_input:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    system_prompt = f"""
You are ChatX, an advanced AI assistant similar to ChatGPT.

User memory:
{st.session_state.memory}

Uploaded file context:
{file_context}

Behavior:
- Be clear, useful, and intelligent.
- Use Markdown.
- Use code blocks for code.
- Explain step by step when helpful.
- If the user uploads a file, use it as context.
- If the user uploads an image, analyze it when relevant.
"""

    api_messages = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]

    for msg in st.session_state.messages:
        api_messages.append({
            "role": msg["role"],
            "content": msg["content"]
        })

    if image_content is not None:
        api_messages.append({
            "role": "user",
            "content": [
                {"type": "text", "text": user_input},
                image_content
            ]
        })

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        stream = client.chat.completions.create(
            model=model,
            messages=api_messages,
            temperature=0.7,
            stream=True
        )

        for chunk in stream:
            if chunk.choices[0].delta.content:
                full_response += chunk.choices[0].delta.content
                message_placeholder.markdown(full_response + "▌")

        message_placeholder.markdown(full_response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": full_response
    })
