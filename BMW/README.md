### GSM SIM7600X 4G MODULE 
The SIM7600X module provides support for the GSM SIM7600X-4G-HAT-Demo module. The SIM7600X module provides a 2-way communication between the driver and the call center. The SIM7600X module also sentds emergency information when a collision occurs.


https://core-electronics.com.au/guides/raspberry-pi-4g-gps-hat/
Enable serial Port on PI, select no for Login Shell, yes for serial port hardware settings

sudo apt-get install minicom
Y + enter
wget https://www.weaveshare.com/w/upload/2/29/SIM7600X-4G-HAT-DEMO.7z
sudo apt-get install p7zip-full
7z x SIM7600X-4G-HAT-Demo.7z -r -o/home/pi
sudo chmod 777 -R /home/pi/SIM7600X-4G-HAT-Demo
sudo nano /etc/rc.local

Add the following to the rc.local file on the last line after fi.
sh /home/pi/SIM7600X-4G-HAT-Demo/Raspberry/c/sim7600_4G_hat_init
Press CTRL + X + Y + ENTER to save .local file

Open new term and enter
cd /home/pi/SIM7600X-4G-HAT-Demo/Raspberry/c/bcm2835
chmod +x configure && ./configure && sudo make && sudo make install

### LoRa Send & Receive
LoRa send is for the LoRa SX1278 module that is to be installed in the BMW,
LoRa receive is for the recipient who is in a recovery vehicle on route to pick the bmw for information / its location.

### HX711 Weight sensor & Momentary switch
if the HX711 Weight sensor detects a sepcified weight, and the belt buckle (with built in switches) is not clicked by the belt, an ALERT will be issued

https://pypi.org/project/hx711/
pip3 install HX711

### Flex sensors