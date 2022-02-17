# This disconnects programs directly connected to ALSA, blocking pulseaudio.
# solves the `(snd_pcm_recover) underrun occurred` error
aconnect -x
poetry run python terramar/terramar.py
