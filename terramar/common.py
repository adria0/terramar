from enum import Enum

MP3_PATH='mp3'

class Color(Enum):
    YELLOW = 1
    BLUE = 2

class IoInterface:
    def led(self, color,on):
        pass
    def pressed(self, color):
        pass

        
