# https://murosdeabsenta.com/musica-anos-40/

from common import MP3_LOCAL_PATH, MP3_REMOTE_PATH
from os import listdir
from os.path import isfile, join
from random import randint

if isfile(join(MP3_REMOTE_PATH,"sound_start.mp3")):
    MP3_PATH = MP3_REMOTE_PATH
else:
    MP3_PATH = MP3_LOCAL_PATH

def two_random_songs():
    mp3files = [f for f in listdir(MP3_PATH) if isfile(join(MP3_PATH, f)) and f.startswith("song_") and f.endswith('.mp3')]

    first= randint(0,len(mp3files)-1)
    second= randint(0,len(mp3files)-1)
    while second == first:
        second = randint(0,len(mp3files)-1)

    first_year = mp3files[first].split('_')[1]
    second_year = mp3files[second].split('_')[1]    
    print(first_year, second_year)
    
    first_is_older = first_year < second_year

    return [join(MP3_PATH,mp3files[first]), join(MP3_PATH,mp3files[second]), first_is_older]

START = join(MP3_PATH,'sound_start.mp3')
QUESTION = join(MP3_PATH,'sound_question.mp3')
NEXT = join(MP3_PATH,'sound_next_song.mp3')
ANSWER = join(MP3_PATH,'sound_answer.mp3')
ROLL = join(MP3_PATH,'sound_roll.mp3')
OK = join(MP3_PATH,'sound_ok.mp3')
KO = join(MP3_PATH,'sound_ko.mp3')
 
