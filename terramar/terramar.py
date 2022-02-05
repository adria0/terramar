# https://murosdeabsenta.com/musica-anos-40/

MP3_PATH = '../mp3'
FADEOUT_SEC = 5

import pygame
from os import listdir
from os.path import isfile, join
from random import randint

def get_songs(user_id):
    mp3files = [f for f in listdir(MP3_PATH) if isfile(join(MP3_PATH, f)) and f.startswith(user_id+"_") and f.endswith('.mp3')]

    first= randint(0,len(mp3files)-1)
    second= randint(0,len(mp3files)-1)
    while second == first:
        second = randint(0,len(mp3files)-1)

    first_year = mp3files[first].split('_')[1]
    second_year = mp3files[second].split('_')[1]    
    print(first_year, second_year)
    if first_year < second_year:
        older = 1
    else:
        older = 2

    return [mp3files[first], mp3files[second], older]

def music_init():
    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.7)

def music_play_sound(sound):
    pygame.mixer.music.load(join(MP3_PATH,sound))
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.wait(100)  # ms

def music_play_song(song):
    pygame.mixer.music.load(join(MP3_PATH,song))
    pygame.mixer.music.play()
    pygame.time.wait(15000)
    fadeout_step = FADEOUT_SEC * 10
    fadeout_dec = pygame.mixer.music.get_volume() / fadeout_step
    for x in range(fadeout_step):
        pygame.mixer.music.set_volume((fadeout_step-x) * fadeout_dec) 
        pygame.time.wait(100)  # ms
        
    pygame.mixer.music.stop();
    pygame.mixer.music.set_volume(fadeout_step * fadeout_dec)

def io_wait_button_pressed():
    # returns 1,2 or 0 if timeout
    return 1

# play hello
music_init() 
music_play_sound('xxxx_start.mp3')

[first_song, second_song, older] = get_songs('0000')

music_play_sound('xxxx_question.mp3')
music_play_song(first_song);
music_play_sound('xxxx_next_song.mp3')
music_play_song(second_song);
music_play_sound('xxxx_press_buttons.mp3');

choice = io_wait_button_pressed()
if choice == 0:
    print(0)
elif choice == older:
    print('ok')
else:
    print('ko')

