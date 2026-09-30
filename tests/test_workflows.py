from app.workflows import PromptStep, TransformStep, Workflow

class FakeAI:
    def generate(self, prompt: str) -> str:
        return f"generated: {prompt}"

def test_prompt_step():
    workflow = Workflow([
        PromptStep(
            template="Hello {name}",
            output_key="answer",
            ai_client=FakeAI(),
        )
    ])
    result = workflow.run({"name": "Muzzammil"})
    assert result["answer"] == "generated: Hello Muzzammil"

def test_transform_step():
    workflow = Workflow([
        TransformStep(
            lambda data: {**data, "uppercase": data["text"].upper()}
        )
    ])
    result = workflow.run({"text": "hello"})
    assert result["uppercase"] == "HELLO"
