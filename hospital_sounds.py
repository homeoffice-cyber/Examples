from pydub import AudioSegment
from pydub.playback import play
import os


pth = '/home/john/Documents/data/audio'
filename = "New Recording 8.m4a"
song = AudioSegment.from_file(os.path.join(pth, filename))
play(song)
