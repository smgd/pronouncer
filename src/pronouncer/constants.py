from enum import Enum


class Voice(str, Enum):
    ARTEMIY = 'artemiy'
    ALEKSANDR_HQ = 'aleksandr-hq'
    BLD = 'bdl'


VOICES = {
    'ru': [
        'aleksandr',
        'aleksandr-hq',
        'anna',
        'arina',
        'artemiy',
        'elena',
        'evgeniy-rus',
        'irina',
        'mikhail',
        'pavel',
        'tatiana',
        'victoria',
        'vitaliy',
        'yuriy',
    ],
    'pl': [
        'natan',
        'magda',
    ],
    'en': [
        'alan',
        'bdl',
        'clb',
        'evgeniy-eng',
        'lyubov',
        'slt',
    ],
    'ua': [
        'anatol',
        'marianna',
        'natalia',
        'volodymyr',
    ],
}
