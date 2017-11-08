# punctuil

punctuil scrapes [Tulsa City Council meetings'
agendas](http://www.tulsacouncil.org/meetings--agendas/search-agendas.aspx) and
[TGOV](http://www.tgovonline.org/) to send text alerts for agenda items as
they are discussed in council.


## Development

### Help maintain this README

If you have trouble with any part of this README, please [file an
issue](https://github.com/codefortulsa/punctuil/issues/new) for us so we can
help you. Especially if you are new to the project - we need your input to help
make it as easy as possible for new contributors.


### Run web interface locally

We want to make sure punctuil is portable between environments and can be
deployed on modern platforms. So, we strongly suggest you:

1. Create a [virtual
   environment](https://python-guide.readthedocs.org/en/latest/dev/virtualenvs/) for punctuil and activate it
2. Install
   [autoenv](https://python-guide.readthedocs.org/en/latest/dev/virtualenvs/#autoenv)

Once you have done that, you should be able to follow these steps to run
punctuil locally with little or no differences from the production site:

```
git clone https://github.com/codefortulsa/punctuil.git
cp punctuil/.env-dist punctuil/.env
```

Open `punctuil/.env` and change `full/path/to/current/dir/db.sqlite` to match
   your `punctuil` directory

```
cd punctuil
pip install -r requirements.txt
python manage.py syncdb
python manage.py migrate
gunicorn punctuil_django.wsgi
```

Yay! punctuil is running on your machine very much like it does on the
production site. But to make and test changes you'll probably need to ...

### Load data locally

As-written, punctuil only loads data once per day. While working on the code,
you will want to re-load data frequently:

* `python load_meeting_list.py` will load the list of meetings for the home
  screen
* `python load_agendas.py` will load the agenda items into each of the meetings
