# https://murosdeabsenta.com/musica-anos-40/

from common import Color, IoInterface
from iogpio import IoGPIO
import sound
import library

import time

def game(io):
    [first_song, second_song, first_is_older] = library.two_random_songs()
    sound.play(library.QUESTION)
    
    io.led(Color.BLUE,True)
    sound.play_fadding_out(first_song)
    io.led(Color.BLUE,False)
    sound.play(library.NEXT)
    io.led(Color.YELLOW, True)
    sound.play_fadding_out(second_song)
    io.led(Color.YELLOW,False)

    while True:
        sound.start(library.ANSWER)
        choice = None
        while choice is None:
            for i in range(10):
                if io.pressed(Color.YELLOW):
                    sound.stop();
                    choice = Color.YELLOW
                    break
                if io.pressed(Color.BLUE):
                    sound.stop();
                    choice = Color.BLUE
                    break
                time.sleep(0.1)
            
            io.led(Color.BLUE,True)
            io.led(Color.YELLOW,True)
            time.sleep(0.5)
            io.led(Color.BLUE,False)
            io.led(Color.YELLOW,False)

        io.led(choice,True)
        sound.play(library.ROLL)
        io.led(choice,False)

        if choice == 0:
            print(0)
        elif (choice == Color.BLUE and first_is_older) or (choice==Color.YELLOW and not first_is_older):
            sound.play(library.OK)
            break
        else:
            sound.play(library.KO)

def flash():
    for i in range(3): 
        io.led(Color.BLUE,True)
        io.led(Color.YELLOW,True)
        time.sleep(0.2)
        io.led(Color.BLUE,False)
        io.led(Color.YELLOW,False)
        time.sleep(0.2)

io = IoGPIO()
sound.init() 
sound.play(library.START)
while True:
    game(io)
    counter = 0
    while True:
        if io.pressed(Color.YELLOW) and io.pressed(Color.BLUE):
            break
        time.sleep(0.1)
        counter = counter + 1
        if counter % 300 == 0:
            flash()

