<p align="center">
  <img src="./assets/banner.png" alt="PennyPilot Banner" width="600"/>
</p>
# 🧠 PennyPilot AI

**PennyPilot** is a lightweight AI assistant that helps job seekers streamline their applications. It can summarize job listings and generate personalized proposals using your CV — ideal for freelancers and professionals navigating online job boards.

---

## 🚀 Features

- ✅ Summarize long job descriptions into key points
- ✅ Generate custom job proposals from your resume
- ✅ Built for local use or agent-based environments (AgentOS-compatible)

---

## 🗂️ Project Structure

```
pennypilot-ai/
├── agent_config/ # Agent definition YAML
├── data/ # Sample inputs
├── tools/ # Core tools (summarizer, proposal writer)
├── utils/ # Helper functions
├── run_tools.py # Test script to run tools locally
├── requirements.txt # Python dependencies
└── README.md # This file
```

---

## ⚙️ How to Use

### 1. Clone this repository
```bash
git clone https://github.com/Serhii-Mazurenko376/pennypilot-ai.git
cd pennypilot-ai
```
### 2. Set up environment
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### 3. Run the tools locally
```
python run_tools.py
```
## 📌 Example Output
```
📝 Running JobSummarizerTool...
Summary:
We are seeking a detail-oriented Python developer with experience in REST APIs, data processing...

✉️ Running ProposalWriterTool...
Dear Hiring Manager,
...
```
## 📦 Integrations

Compatible with LangChain agent formats via agent_config/agent.yaml
Easy to plug into AgentOS or other orchestrators

## 🪪 License

MIT License. Feel free to reuse or extend.
## ✨ Credits

Created by Serhii Mazurenko  
Powered by OpenAI, Python, and motivation ☕️