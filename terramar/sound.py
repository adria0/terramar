SONG_PLAY_SEC = 15
SONG_FADEOUT_SEC = 5

from os.path import join
import pygame

def init():
    pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=2048)
    pygame.mixer.music.set_volume(1.0)

def play(sound):
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.wait(100)  # ms

def play_fadding_out(song):
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
    pygame.time.wait(SONG_PLAY_SEC * 1000)
    fadeout_step = SONG_FADEOUT_SEC * 10
    fadeout_dec = pygame.mixer.music.get_volume() / fadeout_step
    for x in range(fadeout_step):
        pygame.mixer.music.set_volume((fadeout_step-x) * fadeout_dec) 
        pygame.time.wait(100)  # ms
        
    pygame.mixer.music.stop();
    pygame.mixer.music.set_volume(fadeout_step * fadeout_dec)

def start(sound):
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play()
 
def stop():
    pygame.mixer.music.stop()


