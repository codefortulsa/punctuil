###
# Scrapes the agenda items from the livestream feed of the Tulsa City Council meeting.
# 2-24-14 Ian Riley
###

from bs4 import BeautifulSoup
import re
import requests

# the url for the livestream
LIVESTREAM_URL = 'http://tulsa-ok.granicus.com/MediaPlayer.php?publish_id=2'
 
# scrapes the current agenda item that is being discussed
def get_current_item():
    # load the webpage into a BeautifulSoup object (a html parser)
    parser = BeautifulSoup(requests.get(LIVESTREAM_URL).content)
    # scrape the 'Current Item' contained in a span tag with the id : IndexName
    current_item = parser.find('span', {'id': 'IndexName'})
    # check that a current item exists
    if current_item.get_text() != '':
        # return the item number
        return int(re.search(r'\d+\.', current_item.get_text()).group(0).strip('.'))
    else:
        return None

# scrapes the list of items to be covered in the meeting
def get_all_items():
    # load the webpage into a BeautifulSoup object (a html parser)
    parser = BeautifulSoup(requests.get(LIVESTREAM_URL).content)
    # an internal list to contain the agenda items
    agenda_items = []
    # scrape the items from the 'All Items' field contained in a tags with the class : itemLink
    for item in parser.findAll('a', {'class': 'itemLink'}):
        agenda_items.append({'number': int(re.search(r'\d+\.', item.get_text()).group(0).strip('.')), 'text': item.get_text()})
    return agenda_items
