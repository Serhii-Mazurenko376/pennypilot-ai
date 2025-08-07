class ProposalWriterTool:
    def run(self, inputs):
        job_posting = inputs.get("job_posting", "")
        cv = inputs.get("cv", "")
        return f"Dear Hiring Manager,\n\nBased on your job post:\n'{job_posting}'\n\nI believe my background fits well:\n'{cv}'\n\nLooking forward to hearing from you.\n"
