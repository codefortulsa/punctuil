###
# A script to test the merits of designing a web scraper to scrape the agenda information
# from the Tulsa City Council meeting agendas in order to inform interested parties of upcoming
# points on the agenda so that they may support their agenda points instead of being required
# to be present for the entire agenda.
# Service Hackathon - 2/22/14 - Ian Riley
###
import requests
import re
from bs4 import BeautifulSoup

# PARAMS = {"MeetingMonth": "2", "MeetingYear": "2014", "Submit": "Go"}
MEETING_DETAIL_URL = "http://www.tulsacouncil.org/inc/search/meeting_detail.php?id=ZPO0H0YG210201412239"

def scrape_agenda(meeting_detail_url):
    meeting_list = requests.get(meeting_detail_url)
    soup = BeautifulSoup(meeting_list.content)
    patt  = re.compile(r'\d+\.')

    meeting_agenda = []
    meeting_point = 0

    for result in soup.find_all('td'):
        if re.match(patt, result.get_text()):
            meeting_agenda.append([])
            meeting_agenda[meeting_point].append(result.get_text().strip())
            for r in result.find_next_siblings('td', None, None, 3):
                meeting_agenda[meeting_point].append(r.get_text().strip())
            meeting_point += 1

    for row in meeting_agenda:
        for col in row:
            print(col)

def find_agendas():
    MEETING_LIST_URL = 'http://www.tulsacouncil.org/inc/search/meeting_list.php'
    date_params = {"MeetingMonth": "2", "MeetingYear": "2014", "Submit": "Go"}
    meeting_list = requests.get(MEETING_LIST_URL, params=date_params)
    soup = BeautifulSoup(meeting_list.content)

    meeting_list = []
    for result in soup.find_all('td'):
        meeting_list.append(result.get_text())

    meeting_list.sort()
    for entry in meeting_list:
        print(entry)

find_agendas()
