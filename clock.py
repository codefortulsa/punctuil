###
# The scheduled times to run the scraper on Tulsa City Council's website.
# Service Hackathon - 2/22/14 Ian Riley
###

# configure the django settings module in order to import the necessary models
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "punctuil_django.settings")

from apscheduler.schedulers.background import BackgroundScheduler
import load_agendas
import load_meeting_list
import logging
import scrape_livestream
import send_alerts

sched = BackgroundScheduler()
logging.basicConfig()


def scrape_live_feed():
    # scrape the live feed every minute
    # scrape the list of 'All Items' from the live feed to discover
    # the order in which they are covering the items
    all_items = scrape_livestream.get_all_items()
    # scrape the current item
    item_number = scrape_livestream.get_current_item()
    # send out the appropriate alerts
    if item_number is not None:
        # attach the current item number and the list of all item numbers
        send_alerts.main(item_number, all_items)

sched.add_job(scrape_live_feed, 'interval', minutes=1)


def scrape_meeting_list():
    # scrape the meeting list at the beginning of every day
    load_meeting_list.main()

sched.add_job(scrape_meeting_list,
              trigger='cron',
              day_of_week='mon-sun',
              hour=0)


def scrape_agenda_items():
    # scrape the agenda information at the beginning of every day
    load_agendas.main()

sched.add_job(scrape_agenda_items,
              trigger='cron',
              day_of_week='mon-sun',
              hour=0,
              minute=1)


# load the meeting list and agenda items for the current month
load_meeting_list.main()
load_agendas.main()

# start the scheduler
sched.start()

while True:
    pass
