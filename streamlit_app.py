import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="StudyAI",
    page_icon="📘",
    layout="centered"
)

api_key = st.secrets["OPENAI_API_KEY"]

if "history" not in st.session_state:
    st.session_state.history = []

if "usage_count" not in st.session_state:
    st.session_state.usage_count = 0

MAX_USAGE = 5

st.title("📘 StudyAI")
st.caption("AI-powered study help for summaries, key points, and quiz questions.")

remaining = MAX_USAGE - st.session_state.usage_count
if remaining > 0:
    st.caption(f"Free uses left: {remaining}")
else:
    st.caption("Free uses left: 0")

st.markdown("### Enter a topic")
topic = st.text_input(
    "",
    placeholder="e.g. Economics, Photosynthesis, Java Arrays",
    label_visibility="collapsed"
)

col1, col2 = st.columns(2)

with col1:
    generate = st.button("Generate Study Help", use_container_width=True)

with col2:
    example = st.button("Try Example", use_container_width=True)

if example:
    topic = "Economics"

with st.sidebar:
    st.header("📚 History")

    if st.button("Clear History", use_container_width=True):
        st.session_state.history = []

    if st.session_state.history:
        for i, item in enumerate(reversed(st.session_state.history), 1):
            with st.expander(f"{i}. {item['topic']}"):
                st.markdown("**Summary**")
                st.write(item["summary"])

                st.markdown("**Key Points**")
                for point in item["key_points"]:
                    st.markdown(f"- {point}")

                st.markdown("**Quiz Questions**")
                for j, q in enumerate(item["quiz_questions"], 1):
                    st.markdown(f"{j}. {q}")
    else:
        st.caption("No history yet.")

if generate or example:
    if st.session_state.usage_count >= MAX_USAGE:
        st.error("❌ You’ve reached the free usage limit (5 times).")
        st.stop()

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
                        if stripped.startswith("-"):
                            stripped = stripped[1:].strip()
                        summary += stripped + " "
                elif current_section == "key_points":
                    if stripped.startswith("-"):
                        key_points.append(stripped[1:].strip())
                elif current_section == "quiz":
                    if stripped:
                        cleaned = stripped.lstrip("1234567890.- ").strip()
                        if cleaned:
                            quiz_questions.append(cleaned)

            summary = summary.strip()

            st.divider()
            st.subheader(f"📊 Study Result: {topic}")
            st.caption("⚡ Powered by OpenAI")

            st.markdown("### 📌 Summary")
            st.info(summary if summary else "No summary generated.")

            st.markdown("### 🔑 Key Points")
            if key_points:
                for point in key_points:
                    st.success(point)
            else:
                st.write("No key points generated.")

            st.markdown("### ❓ Quiz Questions")
            if quiz_questions:
                for i, q in enumerate(quiz_questions, 1):
                    st.warning(f"{i}. {q}")
            else:
                st.write("No quiz questions generated.")

            st.session_state.history.append(
                {
                    "topic": topic,
                    "summary": summary,
                    "key_points": key_points,
                    "quiz_questions": quiz_questions
                }
            )

            st.session_state.usage_count += 1

        except Exception as e:
            st.error(f"Error: {e}")
