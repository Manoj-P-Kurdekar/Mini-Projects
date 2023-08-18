from gtts import gTTS
import os

mytext = "hello"

language = "en"

myobj = gTTS(text = mytext, lang = language, slow = False)

myobj.save("hello.mp3")

os.system("hello.mp3")