import os
from pydub import AudioSegment

# example usage AudioSegment.from_wav("/input/file.wav").export("/output/file.mp3", format="mp3")

# Let's loop through each of the wav files in the folder ./Homemade and convert them to mp3
for file in os.listdir("./Homemade"):
    if file.endswith(".wav"):
        print(f"Converting {file} to mp3")
        AudioSegment.from_wav(f"./Homemade/{file}").export(f"./Homemade/{file.replace('.wav', '.mp3')}", format="mp3")
