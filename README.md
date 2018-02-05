# piFan
Software I use on the PiFan


# Installation

**Be advised**: For this guide, please checkout this Git repository in `/home/pi/pifan`
If you choose another location, please mind the paths in the rest of the steps.

###Install some software and link some configuration files.
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install nginx-light supervisor ntp
service nginx stop
service supervisor stop
cp /home/pi/pifan/config/AutoChromium.desktop /home/pi/.config/autostart/AutoChromium.desktop
sudo pip install config/requirements.txt
sudo rm /etc/nginx/sites-enabled/default
sudo cp /home/pi/pifan/config/nginx-sites-enabled-default /etc/nginx/sites-enabled/default
sudo cp /home/pi/pifan/config/supervisor-falcontrol.conf /etc/supervisor/conf.d/falcontrol.conf
sudo cp /home/pi/pifan/config/supervisor-usb_switch.conf /etc/supervisor/conf.d/usb_switch.conf
sudo cp /home/pi/pifan/config/supervisor-tempreader.conf /etc/supervisor/conf.d/tempreader.conf
service supervisor start
service nginx start 
sudo reboot
```

#### Optionally, remove stuff that you do not need
```
sudo apt-get remove cups-bsd cups-client cups-common scratch greenfoot bluej sense-emu-tools sense-hat claws-mail libreoffice-base
sudo apt-get remove --purge libreoffice*
```

