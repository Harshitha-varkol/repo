import pygame
import time

pygame.mixer.init()
pygame.mixer.music.load("audio.mp3")
print("🎧 konte choopu tho")
lyrics = [
    (0, "maataraani mounam manase thelipe.."),
    (5, "yeda chaatumaatu gaanam kanule kalipe eeveLa.."),
    (10, "kallo raase nee kallo raase okka chinni kavitha premenemo.."),
    (20, "adi chadivinappudu naa pedavi chappudu tholipaate naalo palikinadi.."),
    # (20, ""),
    # (25, "")
]

pygame.mixer.music.play()
start_time = time.time()

for i in range(len(lyrics)):
    timestamp, line = lyrics[i]
    while time.time() - start_time < timestamp:
        time.sleep(9)  
    

    print(line)


while pygame.mixer.music.get_busy():
    time.sleep(1)

