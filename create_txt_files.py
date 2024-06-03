# loop through all the files in all_mp3s and create a txt file corresponding to each mp3 file
#
import os
for file in os.listdir("./all_mp3s/"):
    if file.endswith(".mp3"):
        with open(f"./all_mp3s/{file.replace('.mp3', '.txt')}", "w") as f:
            f.write("This is a song by the band Sally Mango.")
            f.close()