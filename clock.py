###
# The scheduled times to run the scraper on Tulsa City Council's website.
# Service Hackathon - 2/22/14 Ian Riley
###

# configure the django settings module in order to import the necessary models
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "punctuil_django.settings")

from apscheduler.scheduler import Scheduler
import load_agendas
import load_meeting_list
import scrape_livestream
import send_alerts

sched = Scheduler()

@sched.interval_schedule(minutes=1)
def timed_job():
    #scrape the live feed every minute
    item_number = scrape_livestream.get_current_item()
    # send out the appropriate alerts
    if item_number != None:
        send_alerts.main()

@sched.cron_schedule(day_of_week='mon-sun', hour=0)
def scheduled_job():
    #scrape the agenda information at the beginning of every day
    load_agendas.main()

@sched.cron_schedule(day_of_week='mon-sun', hour=0)
def scheduled_job():
    #scrape the meeting list at the beginning of every day
    load_meeting_list.main()

sched.start()

while True:
    pass
