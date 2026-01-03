import time
import threading
import pygame

# Lyrics
lyrics = [
    "Kallu raase nee kallu raase",
    "Oka chinni kavita premememoo",
    "Adi chadivinappudu",
    "Na nechivi chappudu",
    "Tolipaate naalo paliki"
]

def play_audio():
    pygame.mixer.init()
    pygame.mixer.music.load("song.wav")
    pygame.mixer.music.play()

def print_lyrics():
    for line in lyrics:
        for char in line:
            print(char, end='', flush=True)
            time.sleep(0.05)
        print()
        time.sleep(0.9)

threading.Thread(target=play_audio).start()
print_lyrics()

while pygame.mixer.music.get_busy():
    time.sleep(0.1)
