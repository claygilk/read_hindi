from gtts import gTTS
import os
from playsound3 import playsound
import pandas as pd


df = pd.read_csv('hindi5.csv')
language = 'hi' # 'hi' for Hindi

for index, row in df.iterrows():
    hindi = row['hindi']
    trans = row['trans']
    print(f"Writing {trans}.mp3")

    tts = gTTS(text=hindi, lang=language, slow=False)
    tts.save(f"./mp3/{trans}.mp3")




# print("mid")

# # To play the audio (requires a player like mpg321 on Linux/macOS)
# # os.system("start hindi_output.mp3") # Play a sound file asynchronously (in the background)
# sound = playsound(".\hindi_output.mp3", block=True)


# # Your program continues to run here...
# print("Music is playing in the background while this text is printed.")

# # You can check if the sound is still playing or stop it later
# if sound.is_alive():
#     print("Sound is still playing!")
#     # sound.stop()  # Uncomment this line to stop the sound when needed
# print("end")