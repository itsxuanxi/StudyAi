import streamlit as st
from openai import OpenAI
import base64

st.set_page_config(
    page_title="ChatX",
    page_icon="💬",
    layout="wide"
)

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.markdown("""
<style>
[data-testid="stSidebar"] {
    background-color: #171717;
}
[data-testid="stSidebar"] * {
    color: white;
}
.block-container {
    max-width: 900px;
    padding-top: 2rem;
}
.title {
    text-align: center;
    font-size: 48px;
    font-weight: 800;
    margin-top: 80px;
}
.subtitle {
    text-align: center;
    color: #8e8e8e;
    font-size: 20px;
}
.plus-box {
    border: 1px solid #e5e7eb;
    border-radius: 18px;
    padding: 16px;
    background: #f9fafb;
}
</style>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

if "show_tools" not in st.session_state:
    st.session_state.show_tools = False

if "memory" not in st.session_state:
    st.session_state.memory = ""

with st.sidebar:
    st.title("💬 ChatX")

    if st.button("New Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

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

if not st.session_state.messages:
    st.markdown("<div class='title'>What can I help with?</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Ask questions, write code, analyze files, and build ideas.</div>", unsafe_allow_html=True)

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

uploaded_file = None
uploaded_image = None
file_context = ""
image_content = None

col1, col2 = st.columns([1, 12])

with col1:
    if st.button("＋"):
        st.session_state.show_tools = not st.session_state.show_tools

with col2:
    user_input = st.chat_input("Ask ChatX")

if st.session_state.show_tools:
    st.markdown("<div class='plus-box'>", unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "📎 Add files",
        type=["txt", "md", "py", "csv", "json", "html", "css", "js", "pdf"]
    )

    uploaded_image = st.file_uploader(
        "🖼️ Add photos",
        type=["png", "jpg", "jpeg"],
        key="image_upload"
    )

    st.markdown("</div>", unsafe_allow_html=True)

if uploaded_file is not None:
    try:
        file_context = uploaded_file.read().decode("utf-8")
    except Exception:
        file_context = "The uploaded file could not be read as text."

if uploaded_image is not None:
    image_bytes = uploaded_image.read()
    image_base64 = base64.b64encode(image_bytes).decode("utf-8")
    image_content = {
        "type": "image_url",
        "image_url": {
            "url": f"data:image/jpeg;base64,{image_base64}"
        }
    }

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

Rules:
- Be clear, helpful, and practical.
- Use Markdown.
- Use code blocks for code.
- If the user uploads a file, analyze it when relevant.
- If the user uploads an image, analyze it when relevant.
"""

    api_messages = [
        {"role": "system", "content": system_prompt}
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
        placeholder = st.empty()
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
                placeholder.markdown(full_response + "▌")

        placeholder.markdown(full_response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": full_response
    })
