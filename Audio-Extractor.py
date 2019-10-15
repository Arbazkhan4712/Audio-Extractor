import os
import moviepy.editor as mp #pip install moviepy

path= input("Enter the path of  File :- ")

videoclip = mp.VideoFileClip(path)
audioclip = videoclip.audio
audioclip.write_audiofile("{}""12.mp3".format(path))