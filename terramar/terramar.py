# https://murosdeabsenta.com/musica-anos-40/

MP3_PATH = 'mp3'
SONG_PLAY_SEC = 15
SONG_FADEOUT_SEC = 5
PIN_YELLOW_BUTTON=38 # GPIO 20
PIN_BLUE_BUTTON=40 # GPIO 21
PIN_YELLOW_LED=16 # GPIO 23
PIN_BLUE_LED=18 # GPIO 24

from enum import Enum
import pygame
from os import listdir
from os.path import isfile, join
from random import randint
import time
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

class Color(Enum):
    YELLOW = 1
    BLUE = 2

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
        older = Color.BLUE
    else:
        older = Color.YELLOW

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
    pygame.time.wait(SONG_PLAY_SEC * 1000)
    fadeout_step = SONG_FADEOUT_SEC * 10
    fadeout_dec = pygame.mixer.music.get_volume() / fadeout_step
    for x in range(fadeout_step):
        pygame.mixer.music.set_volume((fadeout_step-x) * fadeout_dec) 
        pygame.time.wait(100)  # ms
        
    pygame.mixer.music.stop();
    pygame.mixer.music.set_volume(fadeout_step * fadeout_dec)

def io_setup():
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
    GPIO.setup(PIN_YELLOW_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(PIN_BLUE_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(PIN_YELLOW_LED, GPIO.OUT)
    GPIO.setup(PIN_BLUE_LED, GPIO.OUT)
    io_led(Color.BLUE,False)
    io_led(Color.BLUE,False)
    time.sleep(0.2)
    io_led(Color.BLUE,True)
    time.sleep(0.2)
    io_led(Color.BLUE,False)
    time.sleep(0.2)
    io_led(Color.YELLOW,True)
    time.sleep(0.2)
    io_led(Color.YELLOW,False)


def io_led(color, on):
    if color == Color.YELLOW:
        pin = PIN_YELLOW_LED
    else:
        pin = PIN_BLUE_LED

    if on:
        GPIO.output(pin,GPIO.HIGH)
    else:
        GPIO.output(pin,GPIO.LOW)

def io_wait_button_pressed():
    while True:
        for i in range(10):
            if GPIO.input(PIN_YELLOW_BUTTON) == GPIO.HIGH:
                return Color.YELLOW
            if GPIO.input(PIN_BLUE_BUTTON) == GPIO.HIGH:
                return Color.BLUE
            time.sleep(0.1)
        
        io_led(Color.BLUE,True)
        io_led(Color.YELLOW,True)
        time.sleep(0.5)
        io_led(Color.BLUE,False)
        io_led(Color.YELLOW,False)

# play hello
io_setup()
music_init() 
music_play_sound('xxxx_start.mp3')

[first_song, second_song, older] = get_songs('0000')
if True:
    music_play_sound('xxxx_question.mp3')
    io_led(Color.BLUE,True)
    music_play_song(first_song)
    io_led(Color.BLUE,False)
    music_play_sound('xxxx_next_song.mp3')
    io_led(Color.YELLOW, True);
    music_play_song(second_song);
    io_led(Color.YELLOW,False)
    # music_play_sound('xxxx_press_buttons.mp3');

choice = io_wait_button_pressed()
io_led(choice,True)
music_play_sound('xxxx_roll.mp3')
io_led(choice,False)

if choice == 0:
    print(0)
elif choice == older:
    music_play_sound('xxxx_ok.mp3')
else:
    music_play_sound('xxxx_ko.mp3')

