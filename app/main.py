from fastapi import FastAPI
from pydantic import BaseModel

from .workflows import run_workflow

app = FastAPI(
    title="OpenAI Workflow Automator",
    description="An AI-powered workflow automation API.",
    version="0.1.0",
)


class WorkflowRequest(BaseModel):
    prompt: str


@app.get("/")
def health_check():
    return {"status": "ok", "service": "OpenAI Workflow Automator"}


@app.post("/workflow")
def workflow(request: WorkflowRequest):
    result = run_workflow(request.prompt)
    return {"result": result}
