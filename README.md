# OpenAI Workflow Automator

An open-source Python toolkit for building small, composable AI-powered automations.

## What it does

- Runs configurable workflows made of simple steps.
- Uses the OpenAI Responses API for AI generation.
- Supports reusable prompt templates.
- Provides a small FastAPI endpoint for triggering workflows.
- Supports optional webhook delivery.
- Keeps secrets in environment variables.
- Includes tests for the workflow engine without requiring an API key.

## Quick start

```bash
git clone https://github.com/mqk89/my-project.git
cd my-project
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and set your API key:

```text
OPENAI_API_KEY=your_key_here
OPENAI_MODEL=gpt-5
```

Never commit `.env` or an API key.

Run the example:

```bash
python examples/content_workflow.py
```

Run the API:

```bash
uvicorn app.main:app --reload
```

Then open `http://127.0.0.1:8000/docs`.

## Workflow model

```text
input → AI generation → optional transform → optional webhook
```

The project is intentionally small so developers can extend it with email,
Slack, databases, queues, scheduled jobs, or custom API integrations.

## API

POST `/workflows/content`

```json
{
  "topic": "An eco-friendly product launch",
  "tone": "professional"
}
```

## Security

- Store credentials in environment variables.
- Do not commit `.env` files or API keys.
- Validate webhook URLs before production use.
- Add authentication and rate limiting before exposing the API publicly.
- Review generated actions before allowing them to affect external systems.

## Development

```bash
pytest
```

## Roadmap

- [ ] More workflow step types
- [ ] Scheduled workflows
- [ ] Persistent execution history
- [ ] Retry policies
- [ ] Webhook authentication
- [ ] Plugin system
- [ ] GitHub Actions CI
- [ ] Better observability and metrics

## License

MIT
