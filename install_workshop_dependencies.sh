#!/bin/sh
sudo apt install git && sudo apt full-upgrade && sudo apt install code && sudo apt install python3 && sudo apt install python3-pip && sudo python3 -m pip install --upgrade pip setuptools wheel && sudo pip3 install --install-option="--force-pi" Adafruit_DHT && python3 -m pip install -U --user pip gpiod && sudo apt install libgpiod2 && sudo apt autoremove && cd Desktop/ && git clone https://github.com/adamzki99/rasp_pi_workshop && cd rasp_pi_workshop/ && echo "-----------------------------------------------" && echo "----------- Everything is set setup -----------" && echo "-----------------------------------------------"