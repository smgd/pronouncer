from typing import Optional, Any

from fastapi import FastAPI, BackgroundTasks, Request, Form
from pydantic import BaseModel, validator, root_validator
from starlette.templating import Jinja2Templates

from .constants import VOICES
from .tasks import say_text, play_mario, say_time, play_mayak, play_metro

app = FastAPI(docs_url="/api/docs")
templates = Jinja2Templates(directory="src/templates")


class SayRequest(BaseModel):
    text: str
    voice: Optional[str] = None
    lang: Optional[str] = None

    @validator('voice')
    def validate_voice(cls, v: Optional[str] = None) -> Optional[str]:
        if v is None:
            return None

        v = v.lower()

        if v not in {voice for lang_voices in VOICES.values() for voice in lang_voices}:
            raise ValueError(f"There is no such voice as '{v}'")

        return v

    @validator('lang')
    def validate_lang(cls, v: Optional[str] = None) -> Optional[str]:
        if v is None:
            return None

        v = v.lower()

        if v not in VOICES:
            raise ValueError(f"There is no such lang as '{v}'")

        return v

    @root_validator
    def validate_lang_and_voice_together(cls, values: dict[str, Any]) -> dict[str, Any]:
        lang, voice = values.get('lang'), values.get('voice')

        if lang is None or voice is None:
            return values

        if voice not in set(VOICES[lang]):
            raise ValueError(f"There is no such voice as '{voice}' for '{lang}' language")

        return values


@app.post("/api/say/")
def say(background_tasks: BackgroundTasks, request: SayRequest) -> dict[str, str]:
    background_tasks.add_task(say_text, text=request.text, voice=request.voice, lang=request.lang)
    return {"result": "OK"}


@app.post("/api/mario/")
def mario(background_tasks: BackgroundTasks) -> dict[str, str]:
    background_tasks.add_task(play_mario)
    return {"result": "OK"}


@app.post("/api/mayak/")
def mayak(background_tasks: BackgroundTasks) -> dict[str, str]:
    background_tasks.add_task(play_mayak)
    return {"result": "OK"}


@app.post("/api/time/")
def time(background_tasks: BackgroundTasks) -> dict[str, str]:
    background_tasks.add_task(say_time)
    return {"result": "OK"}


class MetroRequest(BaseModel):
    sample_name: str


@app.post("/api/metro/")
def metro(background_tasks: BackgroundTasks, request: MetroRequest) -> dict[str, str]:
    background_tasks.add_task(play_metro, sample_name=request.sample_name)
    return {"result": "OK"}


@app.get("/api/voices/")
def get_voices() -> dict[str, list[str]]:
    return VOICES


@app.get("/", include_in_schema=False)
def index(request: Request) -> templates.TemplateResponse:
    return templates.TemplateResponse("index.html", {'request': request})


@app.post("/", include_in_schema=False)
def index(
    request: Request,
    background_tasks: BackgroundTasks,
    text: str = Form(),
) -> templates.TemplateResponse:
    background_tasks.add_task(say_text, text=text)
    return templates.TemplateResponse("index.html", {'request': request})
