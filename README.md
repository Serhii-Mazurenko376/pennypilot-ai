## 📌 Project Overview

**PennyPilot** is a lightweight AI assistant designed to help job seekers and freelancers accelerate job applications. It provides two main capabilities:

- 📝 **Job Summarizer**: Extracts key details from job listings
- 📬 **Proposal Generator**: Generates personalized application letters based on the user’s CV

This project is fully functional without an OpenAI key or API integration, using logic-based tool classes for easy testing and reuse.

---

## ⚙️ Features

- Runs locally with `run_tools.py` or `Streamlit` UI
- Agent-compatible via `agent.yaml`
- Plug-and-play structure for later LLM integration (OpenAI, Ollama)
- Built in Python with beginner-friendly architecture

---

## 💡 Example Use Case

Paste a job description and your resume, and PennyPilot returns:
- A short summary of the job (useful for filtering)
- A tailored application draft (saves time!)

---

## 📂 Files

- `tools/job_summarizer.py`: Summarizes job descriptions
- `tools/proposal_writer.py`: Generates proposals from input
- `agent_config/agent.yaml`: Defines the tools
- `run_tools.py`: Local test runner
- `app.py`: Streamlit UI (optional)

---

## 📸 Banner

![PennyPilot Banner](assets/banner.png)