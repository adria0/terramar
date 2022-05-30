# terramar

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
