import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="StudyAI", page_icon="📘", layout="centered")

api_key = st.secrets["OPENAI_API_KEY"]

st.title("📘 StudyAI")
st.caption("AI-powered study help for summaries, key points, and quiz questions.")

st.markdown("### Enter a topic")
topic = st.text_input(
    "",
    placeholder="e.g. Economics, Photosynthesis, Java Arrays",
    label_visibility="collapsed"
)

col1, col2 = st.columns([1, 1])

with col1:
    generate = st.button("Generate Study Help", use_container_width=True)

with col2:
    example = st.button("Try Example", use_container_width=True)

if example:
    topic = "Economics"

if generate or example:
    if not api_key:
        st.error("API key is not configured.")
    elif not topic.strip():
        st.warning("Please enter a study topic.")
    else:
        try:
            client = OpenAI(api_key=api_key)

            prompt = f"""
You are StudyAI, an AI-powered study assistant.

Topic: {topic}

Return the result in exactly this format:

SUMMARY:
- 2 to 4 concise sentences

KEY POINTS:
- point 1
- point 2
- point 3

QUIZ QUESTIONS:
1. question 1
2. question 2

Keep the answer clear, concise, and student-friendly.
"""

            with st.spinner("Generating study help..."):
                response = client.responses.create(
                    model="gpt-4o-mini",
                    input=prompt
                )

            output = response.output_text

            st.divider()
            st.subheader(f"Study Topic: {topic}")

            summary = ""
            key_points = []
            quiz_questions = []

            current_section = None
            for line in output.splitlines():
                stripped = line.strip()

                if stripped.upper().startswith("SUMMARY:"):
                    current_section = "summary"
                    continue
                elif stripped.upper().startswith("KEY POINTS:"):
                    current_section = "key_points"
                    continue
                elif stripped.upper().startswith("QUIZ QUESTIONS:"):
                    current_section = "quiz"
                    continue

                if current_section == "summary":
                    if stripped:
                        summary += stripped + " "
                elif current_section == "key_points":
                    if stripped.startswith("-"):
                        key_points.append(stripped[1:].strip())
                elif current_section == "quiz":
                    if stripped and (stripped[0].isdigit() or stripped.startswith("-")):
                        quiz_questions.append(stripped.lstrip("1234567890.- ").strip())

            st.markdown("### 📌 Summary")
            st.write(summary.strip() if summary.strip() else "No summary generated.")

            st.markdown("### 🔑 Key Points")
            if key_points:
                for point in key_points:
                    st.markdown(f"- {point}")
            else:
                st.write("No key points generated.")

            st.markdown("### ❓ Quiz Questions")
            if quiz_questions:
                for i, q in enumerate(quiz_questions, 1):
                    st.markdown(f"{i}. {q}")
            else:
                st.write("No quiz questions generated.")

        except Exception as e:
            st.error(f"Error: {e}")
