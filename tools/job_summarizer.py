class JobSummarizerTool:
    def run(self, inputs):
        job_posting = inputs.get("job_posting", "")
        # Simple "summary" — just returns the first 20 words
        summary = " ".join(job_posting.split()[:20])
        return f"Summary: {summary}..."
