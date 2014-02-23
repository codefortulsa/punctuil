###
# The scheduled times to run the scraper on Tulsa City Council's website.
# Service Hackathon - 2/22/14 Ian Riley
###
from apscheduler.scheduler import Scheduler

sched = Scheduler()

@sched.interval_schedule(minutes=1)
def timed_job():
    print('scrape the live feed every minute')

@sched.cron_schedule(day_of_week='mon-sun', hour=0)
def scheduled_job():
    print('scrape the agenda information at the beginning of every day')

@sched.cron_scheduler(day=1, hour=0)
def scheduled_job():
    print('scrape the meeting list at the beginning of every month')

sched.start()

while True:
    pass
