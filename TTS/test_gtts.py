import os
import pyvolume
from gtts import gTTS

# pyvolume.custom(percent=100)

tts = gTTS('System sound on')
tts.save('TTS/Sound_On.mp3')

# os.system("afplay " "TTS/PPD.mp3")