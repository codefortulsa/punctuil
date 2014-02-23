###
# Loads the list of meetings from the website into the database.
# Service Hackathon - 2/23/14 Ian Riley
###

# configure the django settings module in order to import the necessary models
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "punctuil_django.settings")

from agendas.models import Meeting
from datetime import datetime
from re import split
from tulsagovscraper import get_meeting_list

def main():
    # retrieve the list of meetings from the website
    meeting_list = get_meeting_list()

    for meeting in meeting_list:
        # split the meeting information into date/time and name
        meeting_info = split(r' - ', meeting['text'])
        # split the date/time into seperate integers
        dt = split(r'[\W]', meeting_info[0])

        # check if the time is PM
        if dt[5] == 'PM':
            # adjust the time
            dt[3] += 12
        # define a date time object for the meeting
        date_time = datetime(int(dt[2]), int(dt[0]), int(dt[1]), int(dt[3]), int(dt[4]))
        # define a meeting object
        meeting = Meeting(name=meeting_info[1], date=date_time, agenda_id=meeting['href'])

        # print results
        print(meeting.name)
        print(meeting.date)
        print(meeting.agenda_id)
        # save the results
        meeting.save()

main()
