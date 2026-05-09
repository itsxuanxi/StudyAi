import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(
    page_title="ChatX",
    page_icon="💬",
    layout="centered"
)

st.title("💬 ChatX")
st.caption("Your AI assistant for fast answers, ideas, and productivity.")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are ChatX, a helpful, smart, and friendly AI assistant."
        }
    ]

if st.sidebar.button("New Chat"):
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are ChatX, a helpful, smart, and friendly AI assistant."
        }
    ]
    st.rerun()

st.sidebar.title("ChatX")
st.sidebar.write("AI-powered chat assistant.")
st.sidebar.caption("Built with Streamlit + OpenAI")

for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

user_input = st.chat_input("Message ChatX...")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("ChatX is thinking..."):
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=st.session_state.messages
            )

            reply = response.choices[0].message.content
            st.markdown(reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )
