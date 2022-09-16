# pip3 install HX711
#!/usr/bin/python3
from hx711 import HX711

try:
    hx711 = HX711(
        dout_pin=5,
        pd_sck_pin=6,
        channel='A',
        gain=64
    )

    hx711.reset()   # Before we start, reset the HX711 (not obligate)
    measures = hx711.get_raw_data(num_measures=3)
    #if statement of child weight of 15kg comes here...
    #and if weight is detected the button in the seatbelt buckle should be pressed, if released while weight still detected, ALERT!
finally:
    GPIO.cleanup()  # always do a GPIO cleanup in your scripts!

print("\n".join(measures))