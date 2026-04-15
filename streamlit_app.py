import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="StudyAI", page_icon="📘")

st.title("📘 StudyAI")
st.write("An AI-powered study assistant for summaries, key points, and quiz questions.")

api_key = st.text_input("Enter your OpenAI API key", type="password")
topic = st.text_input("Enter a study topic", placeholder="e.g. Economics, Photosynthesis, Java Arrays")

if st.button("Generate Study Help"):
    if not api_key:
        st.warning("Please enter your OpenAI API key.")
    elif not topic.strip():
        st.warning("Please enter a study topic.")
    else:
        try:
            client = OpenAI(api_key=api_key)

            prompt = f"""
You are StudyAI, an AI-powered study assistant.

Topic: {topic}

Give:
1. A simple summary
2. 3 key points
3. 2 quiz questions

Keep the answer clear, concise, and student-friendly.
"""

            with st.spinner("Generating study help..."):
                response = client.responses.create(
                    model="gpt-4o-mini",
                    input=prompt
                )

            st.subheader("StudyAI Output")
            st.write(response.output_text)

        except Exception as e:
            st.error(f"Error: {e}")