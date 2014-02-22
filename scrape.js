"use strict";

var request = require('request');
var cheerio = require('cheerio');

var meeting_list_url = 'http://www.tulsacouncil.org/inc/search/meeting_list.php';

request.post(meeting_list_url,
    {form:
        {
            MeetingMonth: "2",
            MeetingYear: "2014",
            Submit: "Go"
        }
    }, function (err, resp, body) {
      console.log(body);
    }
);
