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


def say_text(text: str, voice: Optional[str] = None, lang: Optional[str] = None) -> None:
    voice = choose_voice(voice, lang)

    command = f'echo "{text}" | RHVoice-test --profile "{voice}" ' \
              f'-v 100 --pitch 100 --rate 90 --sample-rate 360 -o speech.wav ' \
              f'&& mpv speech.wav'

    os.system(command)


def play_mario() -> None:
    command = 'mpv assets/mario.wav'

    os.system(command)
