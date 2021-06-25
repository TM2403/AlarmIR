from irrp_lib import irrp_lib
import time
from datetime import datetime, timedelta

OUTPUT_GPIO = 18
INPUT_GPIO = 17
FILE = "../IRcodes"

system = irrp_lib(FILE)
system.prepare(OUTPUT_GPIO, "P", "light", False)

hour_input = 7
#while hour_input < 0 or hour_input > 24:
#    hour_input = int(input("Hour: "))

minute_input = 30
#while minute_input < 0 or minute_input > 60:
#    minute_input = int(input("Minute: "))


t = datetime.now() + timedelta(days=1)
t = t.replace(hour=hour_input, minute=minute_input, second=0)

while datetime.now() < t:
    time.sleep(1)

system.run()

"""
while True:
    t = datetime.now() + timedelta(minutes=1)
    t = t.replace(second=0)

    while datetime.now() < t:
        time.sleep(1)

    system.run()
    time.sleep(1)
    system.run()
"""