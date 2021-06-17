#!/bin/bash
export CFLAGS=-fcommon
source env/bin/activate
python -m pip install pip
pip install -r requirements.txt
deactivate

sudo groupadd gpio
echo "[+] Added gpio group"
sudo usermod -aG gpio pi
echo "[+] Added pi to GPIO group"
sudo chown root.gpio /dev/gpiomem
echo "[+] Changed owned for /dev/gpiomem"
sudo chmod g+rw /dev/gpiomem
echo "[+] Changed permissions /dev/gpiomem"
