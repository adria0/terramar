#!/usr/bin/bash
aconnect -x
cd /home/pi/terramar 
/home/pi/.poetry/bin/poetry run python terramar/terramar.py
