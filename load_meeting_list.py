###
# Loads the list of meetings from the website into the database.
# Service Hackathon - 2/23/14 Ian Riley
###
from datetime import datetime
from re import split

import django
django.setup()

from agendas.models import Meeting
from tulsagovscraper import get_meeting_list


def main():
    # retrieve the list of meetings from the website
    meeting_list = get_meeting_list()
    # define an object to store the meetings into
    meetings = []

    for meeting in meeting_list:
        # split the meeting information into date/time and name
        meeting_info = split(r' - ', meeting['text'])
        # split the date/time into seperate integers
        dt = split(r'[\W]', meeting_info[0])

        # check if the time is PM
        the_time = int(dt[3])
        if dt[5] == 'PM':
            # adjust the time
            the_time += 12

        # define a date time object for the meeting
        date_time = datetime(int(dt[2]), int(dt[0]), int(dt[1]), the_time, int(dt[4]))
        meetings.append({'date': date_time, 'name': meeting_info[1], 'id': meeting['href']})

    # sort the list of meetings by date/time
    sorted_meetings = sorted(meetings, key=lambda k: k['date'], reverse=True)

    # store all of the meetings in the database
    for meet in sorted_meetings:
        Meeting.objects.get_or_create(
            name=meet['name'], date=meet['date'], agenda_id=meet['id']
        )


if __name__ == "__main__":
    main()
