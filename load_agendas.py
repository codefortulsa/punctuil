###
# Loads the agendas for each meeting into the database.
# Service Hackathon - 2/23/14 Ian Riley
###
import re

import django
django.setup()

from agendas.models import AgendaItem, Meeting
import tulsagovscraper as tgs


def main():
    # get the list of meetings
    meeting_list = Meeting.objects.all()

    for meeting in meeting_list:
        # clear the previous agenda before adding the new one
        for agenda_item in AgendaItem.objects.all().filter(meeting=meeting):
            agenda_item.delete()

        # get the agenda information for the meeting
        info = tgs.scrape_agenda('%s/%s' % (tgs.COUNCIL_URL_ROOT, meeting.agenda_id))
        # store the agenda items into a list
        scraped_items = []
        # the pattern for item numbers
        item_patt = re.compile(r'\d+\.')

        for agenda_item in info:
            # define an agenda item 
            item = AgendaItem()
            # add the appropriate meeting to the agenda item
            item.meeting = meeting
            # load the information into the agenda item
            item.section = agenda_item[0]

            # confirm that the item number is in fact a number
            number = re.search(item_patt, agenda_item[1])
            if number != None:
                # strip off the . following the number
                number = number.group(0).strip('.')
            else:
                # if the item number is not contained in the item number header
                # then it must be contained in the section header
                number = re.search(item_patt, item.section).group(0).strip('.')
            item.number = int(number)

            item.text, item.minutes, item.backup = agenda_item[2:5]
            # store the items in the list with their item number
            scraped_items.append({'number': item.number, 'item': item})

        # sort the list of items by their number
        # uncomment next line if agenda item numbers ever become non-sequential
        #scraped_items.sort()

        # save the agenda items
        for item in scraped_items:
            item['item'].save()


if __name__ == "__main__":
    main()
