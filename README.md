punctuil
========

A small text message service to help council meeting speakers.

Overview
--------

1. Use http://www.tulsacouncil.org/meetings--agendas/search-agendas.aspx and http://www.tulsacouncil.org/inc/search/meeting_list.php to find meeting agenda links which leads to ...
2. Scrape the agenda details from the meeting detail page. e.g., http://www.tulsacouncil.org/inc/search/meeting_detail.php?id=ZPO0H0YG210201412239
3. Allow users to subscribe to an item with their phone number
4. Monitor the current item on TGOV: http://www.tgovonline.org/
5. When the item is "upcoming", send a text message via Twilio

To run locally
--------------

1. clone the repo
2. `pip install -r requirements.txt`
3. `cp .env-dist .env`
4. Change the `full/path/to/current/dir/db.sqlite`
5. `export DATABASE_URL=sqlite:////full/path/to/current/dir/db.sqlite`
6. `python manage.py syncdb`
7. `python manage.py migrate`
8. `foreman start`
