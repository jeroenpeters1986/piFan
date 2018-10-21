# piFan
Software I use on the PiFan

**Attention!**
 * Do you have a Pi3B+? Please use the branch `pi3b-plus`, it contains a small fix for controlling USB ports
 * Do you want to display Fahrenheit instead of Celsius? Please checkout the `fahrenheit` branch (on Pi up to Pi3B)

Please also checkout the [Pi hardware compatibility list](#raspberry-pi) below

# Installation

**Be advised**: For this guide, please checkout this Git repository in 
`/home/pi/pifan`. If you choose to checkout to another location, please 
adjust the paths in the installation commands and the scripts accordingly.

### Install the software, setup the configuration and reboot
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install nginx-light supervisor git build-essential python-dev python-pip
service nginx stop
service supervisor stop
cp /home/pi/pifan/config/AutoChromium.desktop /home/pi/.config/autostart/AutoChromium.desktop
sudo pip install -r /home/pi/pifan/config/requirements.txt
git clone https://github.com/adafruit/Adafruit_Python_DHT.git /tmp/dht
cd /tmp/dht
sudo python setup.py install
sudo rm /etc/nginx/sites-enabled/default
sudo cp /home/pi/pifan/config/nginx-sites-enabled-default /etc/nginx/sites-enabled/default
sudo cp /home/pi/pifan/config/supervisor-falcontrol.conf /etc/supervisor/conf.d/falcontrol.conf
sudo cp /home/pi/pifan/config/supervisor-usb_switch.conf /etc/supervisor/conf.d/usb_switch.conf
sudo cp /home/pi/pifan/config/supervisor-tempreader.conf /etc/supervisor/conf.d/tempreader.conf
sudo reboot
```

After the reboot, Chromium should start and it should present you with the touchinterface
If you don't want to reboot and start Chromium yourself, you should run `service supervisor start; service nginx start`

#### Optionally, remove stuff that you do not need
```
sudo apt-get remove cups-bsd cups-client cups-common scratch greenfoot bluej sense-emu-tools sense-hat claws-mail libreoffice-base
sudo apt-get remove --purge libreoffice*
```


## Hardware

### Raspberry Pi

Offcourse you need a Raspberry Pi. There are multiple Pi models, not every Pi would work.

Thanks to @koenvervloesem I can provide you this overview:

| Model                    | Suitable for PiFan    | Comment                                                                                                                          |
|--------------------------|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Pi Zero and Pi Zero W    | No                    | These models don't have a USB hub                                                                                                |
| Pi 1 Model B             | No                    | The USB ports for this model are not controllable                                                                                |
| Pi 1 Model B+ Pi 2 Pi 3B | Yes                   | These all work without modifications                                                                                             |
| Pi 3B+                   | Yes, with code change | you need to change the option `-h 0` on the line beginning with `control_command` in `/home/pi/pifan/switch_on_off.py` to `-h 1` |

With this knowledge, I got the piFan software working on the Pi 2, 3B and 3B+ (I haven't found my Pi 1 Model B+).

### Temperature Sensor
For the temperature readings I chose the DHT22 from Adafruit. This sensor is 
pretty accurate. You can also choose to use the DHT11, it's a little bit 
cheaper but less accurate. I have bought the one already attached to a chip.

### Touch screen and acrylic case
The touch screen that has been used for this project is a 3,5" capacative 
touch display. It comes with a cool acrylic case. This case also takes care
of supporting the display.
You can find them on eBay. At the time of writing, you could 
[buy this one](https://www.ebay.com/p/3-5-TFT-LCD-Touch-Screen-Display-Clear-Case-for-Raspberry-Pi-2-3-Pi3-Model-B/629458989)

_Btw: Please let me know when the link is dead._

### Wiring
Here's the scheme of the wiring. The display is just for illustration purposes 
to see which pins are allocated by the action touchscreen. Use the image to 
hook up the DHT22 temprature sensor.
![Wiring of the PiFan](config/pifan_wiring.png?raw=true "Wiring of the PiFan")

# Credits
 * The file `hub-ctrl` is a compiled version of the sourcecode of https://github.com/codazoda/hub-ctrl.c
