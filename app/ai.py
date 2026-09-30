from openai import OpenAI

from .config import settings


def get_client() -> OpenAI:
    if not settings.openai_api_key:
        raise RuntimeError("OPENAI_API_KEY is not configured.")

    return OpenAI(api_key=settings.openai_api_key)


def generate_text(prompt: str) -> str:
    client = get_client()

    response = client.responses.create(
        model=settings.openai_model,
        input=prompt,
    )

    return response.output_text
