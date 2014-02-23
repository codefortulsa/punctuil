###
# Loads the agendas for each meeting into the database.
# Service Hackathon - 2/23/14 Ian Riley
###

# configure the django settings module in order to import the necessary models
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "punctuil_django.settings")

from agendas.models import AgendaItem
import tulsagovscraper as tgs

# the url for the Tulsa City Council website
COUNCIL_URL_ROOT = "http://www.tulsacouncil.org/inc/search"

def main():
    # retreive the meeting list SHOULD GET FROM DATABASE
    meeting_list = tgs.get_meeting_list()
    # get the agenda information for the meeting
    info = tgs.scrape_agenda('%s/%s' % (COUNCIL_URL_ROOT, meeting_list[0]['href']))
    # define an agenda item 
    item = AgendaItem()
    # load the information into the agenda item
    item.section, item.number, item.text, item.minutes, item.backup = info[0]

    # NEEDS TO SAVE TO THE DATABASE
    print(item.section)
    print(item.number)
    print(item.text)
    print(item.minutes)
    print(item.backup)

main()
