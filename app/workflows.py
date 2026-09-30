from .ai import generate_text


def run_workflow(prompt: str) -> str:
    """Run a simple AI-powered workflow."""
    return generate_text(prompt)
