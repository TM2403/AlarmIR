from irrp_lib import irrp_lib
from datetime import datetime, timedelta

OUTPUT_GPIO = 18
INPUT_GPIO = 17

system = irrp_lib("../IRcodes")
system.prepare(OUTPUT_GPIO, "P", "light", False)

minutes = datetime.now().minute + 1

while True:
    time = datetime.now() + timedelta(minutes=1)
    time = time.replace(second=0)

    while datetime.now < time:
        time.sleep(1)

    system.run()
    time.sleep(1)
    system.run()
