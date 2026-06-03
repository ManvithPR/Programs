from gtts import gTTS
import os

gTTS(text=input("Manvith",),lang='en',slow=False).save("Manvith.mp3")
os.system("mpg321 Manvith.mp3")
print("done")