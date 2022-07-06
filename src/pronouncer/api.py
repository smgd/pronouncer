from typing import Optional

from fastapi import FastAPI, BackgroundTasks, Request, Form
from pydantic import BaseModel
from starlette.templating import Jinja2Templates

from .tasks import say_text

app = FastAPI()
templates = Jinja2Templates(directory="src/templates")


class SayRequest(BaseModel):
    text: str
    voice: Optional[str] = None


@app.post("/say/")
def say(background_tasks: BackgroundTasks, request: SayRequest) -> dict[str, str]:
    background_tasks.add_task(say_text, text=request.text, voice=request.voice)
    return {"result": "OK"}


@app.get("/")
def index(request: Request) -> templates.TemplateResponse:
    return templates.TemplateResponse("index.html", {'request': request})


@app.post("/")
def index(
    request: Request,
    background_tasks: BackgroundTasks,
    text: str = Form(),
) -> templates.TemplateResponse:
    background_tasks.add_task(say_text, text=text)
    return templates.TemplateResponse("index.html", {'request': request})
