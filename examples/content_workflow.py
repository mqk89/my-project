from app.workflows import PromptStep, Workflow

workflow = Workflow([
    PromptStep(
        template=(
            "Write a short, engaging product launch announcement for: "
            "{topic}. Tone: {tone}."
        ),
        output_key="announcement",
    )
])

if __name__ == "__main__":
    result = workflow.run({
        "topic": "a new eco-friendly home product",
        "tone": "friendly and professional",
    })
    print(result["announcement"])
