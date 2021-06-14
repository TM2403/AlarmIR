from irrp_lib import irrp_lib
import time
import sched

scheduler = sched.scheduler(time.time, time.sleep)
system = irrp_lib("../IRcodes")

system.prepare(18, "P", "light", False)

scheduler.enter(12, 1, system.run, ('first',))
scheduler.enter(24, 1, system.run, ('second',))

scheduler.run()
