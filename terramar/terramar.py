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
    pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=2048)
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

class IoInterface:
    def led(self, color,on):
        pass
    def pressed(self, color):
        pass

class IoGPIO(IoInterface):
    def __init__(self):
        GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
        GPIO.setup(PIN_YELLOW_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(PIN_BLUE_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(PIN_YELLOW_LED, GPIO.OUT)
        GPIO.setup(PIN_BLUE_LED, GPIO.OUT)
        self.led(Color.BLUE,False)
        self.led(Color.BLUE,False)
        time.sleep(0.2)
        self.led(Color.BLUE,True)
        time.sleep(0.2)
        self.led(Color.BLUE,False)
        time.sleep(0.2)
        self.led(Color.YELLOW,True)
        time.sleep(0.2)
        self.led(Color.YELLOW,False)
    
    def led(self, color,on):
        if color == Color.YELLOW:
            pin = PIN_YELLOW_LED
        else:
            pin = PIN_BLUE_LED

        if on:
            GPIO.output(pin,GPIO.HIGH)
        else:
            GPIO.output(pin,GPIO.LOW)
    
    def pressed(self, color):
        if color == Color.YELLOW:
            pin = PIN_YELLOW_BUTTON
        else:
            pin = PIN_BLUE_BUTTON
        return GPIO.input(pin) == GPIO.HIGH

def wait_button_pressed(io, sound):
    pygame.mixer.music.load(join(MP3_PATH,sound))
    pygame.mixer.music.play()
    while True:
        for i in range(10):
            if io.pressed(Color.YELLOW) == GPIO.HIGH:
                pygame.mixer.music.stop();
                return Color.YELLOW
            if io.pressed(Color.BLUE) == GPIO.HIGH:
                pygame.mixer.music.stop();
                return Color.BLUE
            time.sleep(0.1)
        
        io.led(Color.BLUE,True)
        io.led(Color.YELLOW,True)
        time.sleep(0.5)
        io.led(Color.BLUE,False)
        io.led(Color.YELLOW,False)

io = IoGPIO()
music_init() 
music_play_sound('xxxx_start.mp3')
[first_song, second_song, older] = get_songs('0000')

if False:
    music_play_sound('xxxx_question.mp3')
    io.led(Color.BLUE,True)
    music_play_song(first_song)
    io.led(Color.BLUE,False)
    music_play_sound('xxxx_next_song.mp3')
    io.led(Color.YELLOW, True);
    music_play_song(second_song);
    io.led(Color.YELLOW,False)

while True:
    choice = wait_button_pressed(io,'xxxx_answer.mp3')
    io.led(choice,True)
    music_play_sound('xxxx_roll.mp3')
    io.led(choice,False)

    if choice == 0:
        print(0)
    elif choice == older:
        music_play_sound('xxxx_ok.mp3')
        break
    else:
        music_play_sound('xxxx_ko.mp3')

