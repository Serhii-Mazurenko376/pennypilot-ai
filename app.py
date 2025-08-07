import streamlit as st
from tools.job_summarizer import JobSummarizerTool
from tools.proposal_writer import ProposalWriterTool

st.set_page_config(page_title="PennyPilot", layout="centered")

st.title("🧠 PennyPilot: AI Job Application Assistant")
st.write("Paste a job description and your CV below to generate a summary and proposal.")

job_posting = st.text_area("📝 Job Description", height=200)
cv = st.text_area("📎 Your CV or Experience", height=200)

if st.button("✍️ Generate Summary and Proposal"):
    if not job_posting or not cv:
        st.warning("Please provide both job description and CV.")
    else:
        with st.spinner("Generating..."):
            summary = JobSummarizerTool().run({"job_posting": job_posting})
            proposal = ProposalWriterTool().run({"job_posting": job_posting, "cv": cv})

        st.subheader("📄 Job Summary")
        st.success(summary)

        st.subheader("📬 Proposal Draft")
        st.info(proposal)
