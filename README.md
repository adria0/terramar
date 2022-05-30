<img src="https://raw.githubusercontent.com/adria0/terramar/1caebe358dae23ba601c5f9c8b106634c92dd4a2/device.jpg" width="200" height="200">

Terramar is a small [musical theraphy](https://en.wikipedia.org/wiki/Music_therapy) device for elderly people to help them to recall memories using songs. It uses raspberry a [raspberry](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) and python. It's a joint effort with [Ateneu de fabricació de les corts](https://ajuntament.barcelona.cat/lescorts/ca/coneixeu-el-districte/lateneu-de-fabricacio-digital).


## Functionality

The device has a very basic functionality:

- Plays a sound saying that you have to guess which song from two are earlier in time
- Plays a first song (choosen from the `mp3` folder)
- Plays a second song (choosen from the `mp3` folder)
- Waits user to press one of the buttons
- The device emits a sound depending if the response is ok or not

you can see the logic in the [terramar.py](https://github.com/adria0/terramar/blob/main/terramar/terramar.py) file.


## Installation

```
sudo apt-get install python3-distutils python3-apt python3-dev
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
poetry  install
sudo mkdir /mnt/sda2
sudo vi /etc/fstab
# add this line
# /dev/sda2	/mnt/sda2	vfat	defaults,nofail	0	0
sudo mount -a 
```
