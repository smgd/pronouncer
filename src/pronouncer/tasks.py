import os

from .constants import Voice


def say_text(text: str, voice: str = Voice.ARTEMIY.value) -> None:
    if voice is None:
        voice = Voice.ARTEMIY.value

    command = f'echo "{text}" | RHVoice-test --profile "{voice}" ' \
              f'-v 100 --pitch 100 --rate 90 --sample-rate 360 -o speech.wav ' \
              f'&& mpv speech.wav'
    os.system(command)
