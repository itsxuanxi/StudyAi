import streamlit as st
from openai import OpenAI
import base64

st.set_page_config(
    page_title="ChatX",
    page_icon="💬",
    layout="wide"
)

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ---------------- CSS ----------------
st.markdown("""
<style>
[data-testid="stSidebar"] {
    background-color: #111827;
}
[data-testid="stSidebar"] * {
    color: white;
}
.main-title {
    font-size: 44px;
    font-weight: 800;
    text-align: center;
    margin-top: 40px;
}
.subtitle {
    text-align: center;
    color: #9ca3af;
    margin-bottom: 40px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Session ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "memory" not in st.session_state:
    st.session_state.memory = ""

# ---------------- Sidebar ----------------
with st.sidebar:
    st.title("💬 ChatX")
    st.caption("AI-powered chat assistant.")

    if st.button("➕ New Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")

    model = st.selectbox(
        "Model",
        [
            "gpt-4o-mini",
            "gpt-4o"
        ]
    )

    st.markdown("---")

    st.subheader("🧠 AI Memory")
    st.session_state.memory = st.text_area(
        "What should ChatX remember?",
        value=st.session_state.memory,
        placeholder="Example: I am a CS & Business student at Concordia.",
        height=120
    )

    st.markdown("---")

    uploaded_file = st.file_uploader(
        "Upload a file",
        type=["txt", "md", "py", "csv", "json"]
    )

    uploaded_image = st.file_uploader(
        "Upload an image",
        type=["png", "jpg", "jpeg"],
        key="image_upload"
    )

    st.markdown("---")
    st.caption("Built with Streamlit + OpenAI")

# ---------------- Main ----------------
st.markdown("<div class='main-title'>💬 ChatX</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Ask anything. Learn anything. Create anything.</div>", unsafe_allow_html=True)

# ---------------- Display History ----------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------- File Context ----------------
file_context = ""

if uploaded_file is not None:
    try:
        file_context = uploaded_file.read().decode("utf-8")
        st.sidebar.success("File uploaded successfully.")
    except:
        st.sidebar.error("Could not read this file.")

# ---------------- Image Context ----------------
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

# ---------------- Chat Input ----------------
user_input = st.chat_input("Message ChatX...")

if user_input:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    system_prompt = f"""
You are ChatX, a helpful, intelligent AI assistant.

User memory:
{st.session_state.memory}

Uploaded file context:
{file_context}

Rules:
- Be helpful, clear, and practical.
- Use Markdown formatting.
- Use code blocks when writing code.
- If the user uploads a file, answer based on the file when relevant.
- If the user uploads an image, analyze the image when relevant.
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
                {
                    "type": "text",
                    "text": user_input
                },
                image_content
            ]
        })

    with st.chat_message("assistant"):
        response_box = st.empty()
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
                response_box.markdown(full_response + "▌")

        response_box.markdown(full_response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": full_response
    })
