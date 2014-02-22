###
# A script to test the merits of designing a web scraper to scrape the agenda information
# from the Tulsa City Council meeting agendas in order to inform interested parties of upcoming
# points on the agenda so that they may support their agenda points instead of being required
# to be present for the entire agenda.
# Service Hackathon - 2/22/14 - Ian Riley
###
import requests
from bs4 import BeautifulSoup

PARAMS = {"MeetingMonth": "2", "MeetingYear": "2014", "Submit": "Go"}
meeting_list = requests.post("http://www.tulsacouncil.org/inc/search/meeting_detail.php?id=ZPO0H0YG210201412239", params=PARAMS)
soup = BeautifulSoup(meeting_list.content)

for table in soup.find_all('table'):
    rows = table.find('tbody').find_all('tr')
    for row in rows:
        data = row.find_all('td')
        for d in data:
            print (d)
