from typing import Text
from vosk import Model, KaldiRecognizer
import os
import pyaudio
import pyttsx3
import json
import core


engine = pyttsx3.init()

voices = engine.getProperty('voices')


def speak(text):
       engine.say(text)
       engine.runAndWait()

model = Model("model")
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=4000)
stream.start_stream()

while True:
       data = stream.read(4000)
       if len(data) == 0:
              break
       if rec.AcceptWaveform(data):
              result = rec.Result()
              result = json.loads(result)

              if result is not None:
                     text = result['text']
                     print(text)
                     if text == 'que horas são' or text == 'me diga as horas':
                            speak(core.SystemInfo.get_time())
