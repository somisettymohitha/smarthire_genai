import streamlit as st

from src.parsing.resume_parser import parse_resume
from src.search.job_search import search_jobs
from src.generate.cv_suggestions import generate_suggestions
from src.mentor.rag_chain import ask_career_mentor
from src.safety.guardrails import check_guardrails

st.set_page_config(
    page_title="SmartHire GenAI",
    page_icon="💼",
    layout="wide"
)

st.title("💼 SmartHire GenAI")
st.write("AI Powered Resume Analyzer & Career Mentor")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("Resume Uploaded Successfully")

    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.read())

    resume = parse_resume("temp_resume.pdf")

    st.subheader("Parsed Resume")

    st.write(resume)

    st.subheader("Matching Jobs")

    jobs = search_jobs(resume)

    st.dataframe(jobs)

    st.subheader("Resume Suggestions")

    suggestions = generate_suggestions(resume)

    st.write(suggestions)

st.subheader("Career Mentor")

question = st.text_input(
    "Ask your Career Question"
)

if question:

    safe = check_guardrails(question)

    if safe:

        answer = ask_career_mentor(question)

        st.write(answer)

    else:

        st.error(
            "Unsafe Question Detected."
        )
