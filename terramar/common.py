from enum import Enum

MP3_LOCAL_PATH='mp3'
MP3_REMOTE_PATH='/mnt/sda2' 

class Color(Enum):
    YELLOW = 1
    BLUE = 2

class IoInterface:
    def led(self, color,on):
        pass
    def pressed(self, color):
        pass

        
