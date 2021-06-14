from irrp_lib import irrp_lib
import time
import sched

scheduler = sched.scheduler(time.time, time.sleep)
system = irrp_lib("../IRcodes")


scheduler.enter(2, 1, system.run(18, "P", "light", False), ('first',))
scheduler.enter(4, 1, system.run(18, "P", "light", False), ('second',))



