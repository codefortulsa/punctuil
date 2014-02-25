###
# Service Hackathon - 2/23/14 Ian Riley
###

from agendas.models import Alert
# download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

def main():
    for alert in Alert.objects.all():
        if not alert.sent:
            # Find these values at https://twilio.com/user/account
            account_sid = "ACb395c103ff24402c9caf5504c7d10cdb"
            auth_token = "cc124f08b5d4ba53f413c94924b9cf16"
            client = TwilioRestClient(account_sid, auth_token)

            message = client.messages.create(to=alert.phone, from_="9185508625", body="Agenda Item number: %d is next!" % alert.item.number)
            alert.sent = True
            alert.save()

            print('alert sent')
