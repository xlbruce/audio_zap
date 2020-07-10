#-*- coding: utf-8 -*-
import os
from _io import BufferedRandom

import speech_recognition as sr
from pydub import AudioSegment

def get_transcription(audio_filename:str) -> str:
    sound = convert_to_wav(audio_filename)
    with sr.AudioFile(sound) as source:
        r = sr.Recognizer()
        audio = r.record(source)
        try:
            return r.recognize_google(audio, language='pt-BR')
        except Exception as e:
            return f'Error: {e}' 

def convert_to_wav(filename: str) -> BufferedRandom:
    if not os.path.exists(filename):
        raise ValueError(f'File "{filename}" not found')

    sound = AudioSegment.from_ogg(filename)
    sound = sound.export(format='wav')
    sound.seek(0)
    return sound
