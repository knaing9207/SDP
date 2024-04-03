import os
import pyvolume
from gtts import gTTS

# pyvolume.custom(percent=100)

tts = gTTS('Your Medication is Ready')
# tts.save('TTS/Ready.mp3')

os.system("afplay " "TTS/Ready.mp3")