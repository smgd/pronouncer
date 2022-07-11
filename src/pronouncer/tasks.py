import datetime
import os
import random
from typing import Optional

from .constants import VOICES


def choose_voice(voice: Optional[str] = None, lang: Optional[str] = None) -> str:
    if voice is None:
        if lang is None:
            lang = 'ru'

        return random.choice(VOICES[lang])

    return voice


def get_say_command(text: str, voice: Optional[str] = None, lang: Optional[str] = None) -> str:
    voice = choose_voice(voice, lang)

    return f'echo "{text}" | RHVoice-test --profile "{voice}" ' \
           f'-v 100 --pitch 100 --rate 90 --sample-rate 360 -o speech.wav'


def say_text(text: str, voice: Optional[str] = None, lang: Optional[str] = None) -> None:
    say_command = get_say_command(text, voice, lang)
    command = f'{say_command} && mpv speech.wav'

    os.system(command)


def say_time() -> None:
    text = f'Точное время по Тбилиси - {datetime.datetime.now().strftime("%H:%M")}'
    command = f'{get_say_command(text)} && mpv assets/pipipi.wav && mpv speech.wav'

    os.system(command)


def play_mario() -> None:
    command = 'mpv assets/mario.wav'

    os.system(command)


def play_mayak() -> None:
    command = 'mpv assets/mayak.wav'

    os.system(command)
