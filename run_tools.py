from tools.job_summarizer import JobSummarizerTool
from tools.proposal_writer import ProposalWriterTool

# Sample input
job_text = """We are seeking a detail-oriented Python developer with experience in REST APIs, data processing, and automation tools like Selenium or BeautifulSoup. Remote work allowed."""
cv_text = """Experienced Python developer skilled in API integration, data scraping, and task automation. Successfully built file organizer and job proposal generators using Python."""

# Run Job Summarizer Tool
print("📝 Running JobSummarizerTool...")
summary_result = JobSummarizerTool().run({"job_posting": job_text})
print("Summary:\n", summary_result)

# Run Proposal Writer Tool
print("\n✉️ Running ProposalWriterTool...")
proposal_result = ProposalWriterTool().run({"job_posting": job_text, "cv": cv_text})
print("Proposal:\n", proposal_result)
