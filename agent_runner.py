import yaml
from tools.job_summarizer import JobSummarizerTool
from tools.proposal_writer import ProposalWriterTool

# Load agent config
with open("agent_config/agent.yaml", "r") as f:
    config = yaml.safe_load(f)

tools_registry = {
    "tools.job_summarizer:JobSummarizerTool": JobSummarizerTool,
    "tools.proposal_writer:ProposalWriterTool": ProposalWriterTool,
}

print(f"🧠 Agent: {config['name']}")
print(f"📄 Description: {config['description']}\n")

for tool_path in config["tools"]:
    ToolClass = tools_registry[tool_path]
    tool = ToolClass()
    print(f"🚀 Running tool: {tool_path}")
    output = tool.run({
        "job_posting": "We need a Python developer for API automation and job scraping tasks.",
        "cv": "Experienced in Python automation and CV/job matching tools. Built PennyPilot tools from scratch."
    })
    print(f"✅ Output:\n{output}\n{'-'*50}")
