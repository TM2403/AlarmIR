from irrp_lib import irrp_lib
import time
import sched

scheduler = sched.scheduler(time.time, time.sleep)
system = irrp_lib("../IRcodes")

system.prepare(18, "P", "light", False)

scheduler.enter(2, 1, system.run, argument=('first',))
scheduler.enter(4, 1, system.run, argument=('second',))

scheduler.run()
