###
# Loads the agendas for each meeting into the database.
# Service Hackathon - 2/23/14 Ian Riley
###

# configure the django settings module in order to import the necessary models
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "punctuil_django.settings")

from agendas.models import AgendaItem, Meeting
import tulsagovscraper as tgs

# the url for the Tulsa City Council website
COUNCIL_URL_ROOT = "http://www.tulsacouncil.org/inc/search"

def main():
    # get the list of meetings
    meeting_list = Meeting.objects.all()

    for meeting in meeting_list:
        for agenda_item in AgendaItem.objects.all().filter(meeting=meeting):
            agenda_item.delete()
            print('%d - entry deleted' % agenda_item.number)
        # get the agenda information for the meeting
        info = tgs.scrape_agenda('%s/%s' % (COUNCIL_URL_ROOT, meeting.agenda_id))
        for agenda_item in info:
            # define an agenda item 
            item = AgendaItem()
            # add the appropriate meeting to the agenda item
            item.meeting = meeting
            # load the information into the agenda item
            item.section, item.number, item.text, item.minutes, item.backup = agenda_item
 
            # save to the database
            print('%d - entry saved' % item.number)
            item.save()

main()
