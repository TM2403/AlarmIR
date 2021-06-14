from irrp_lib import irrp_lib
import time
from datetime import datetime, timedelta

OUTPUT_GPIO = 18
INPUT_GPIO = 17

system = irrp_lib("../IRcodes")
system.prepare(OUTPUT_GPIO, "P", "light", False)

minutes = datetime.now().minute + 1

#while True:
t = datetime.now() # + timedelta(days=1)
t = t.replace(hour=22, minute=31, second=0)

while datetime.now() < t:
    time.sleep(1)

system.run()
