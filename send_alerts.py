###
# Sends an alert message to all subscribed numbers that have not been notified.
# Service Hackathon - 2/23/14 Ian Riley
###

from agendas.models import Alert
# download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

def main(current_item, all_items):
    # Find these values at https://twilio.com/user/account
    account_sid = "ACb395c103ff24402c9caf5504c7d10cdb"
    auth_token = "cc124f08b5d4ba53f413c94924b9cf16"
    client = TwilioRestClient(account_sid, auth_token)

    # subscribers should only receive messages within two agenda items of their own
    # locate the index of the current agenda item
    index = 0
    while (index < len(all_items)) and (all_items[index]['number'] != current_item):
        index += 1

    # check that the current agenda item was found
    if index < len(all_items):

        for alert in Alert.objects.all():
            # check the current item against the subscribed item
            if (not alert.now_sent) and (all_items[index]['number'] == alert.item.number):
                # notify the subscriber that the Tulsa City Council is now on their agenda item
                message = client.messages.create(to=alert.phone, from_="9185508625", body="Your Agenda Item : %d is up!" % current_item)
                # mark the final alert as sent
                alert.now_sent = True
                # update the alert
                alert.save()

            # check if the subscribed item is the next item
            else if (not alert.one_sent) and (index+1 < len(all_items)) and (all_items[index+1]['number'] == alert.item.number):
                # notify the subscriber that their agenda item is the next item
                message = client.messages.create(to=alert.phone, from_="9185508625", body="Tulsa City Council is now on Agenda Item : %d. Your Agenda Item is next!" % current_item)
                # mark the first alert as sent
                alert.one_sent = True
                # update the alert
                alert.save()

            # check if the subscribed item is the second to next item
            else if (not alert.two_sent) and (index+2 < len(all_items)) and (all_items[index+2]['number'] == alert.item.number):
                # notify the subscriber that their agenda item is the second to next item
                message = client.messages.create(to=alert.phone, from_="9185508625", body="Tulsa City Council is now on Agenda Item: %d. Your Agenda Item is 2 away!" % current_item)
                # mark the second alert as sent
                alert.two_sent()
                # update the alert
                alert.save()
