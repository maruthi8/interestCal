import messagebird
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from twilio.rest import Client

from api.models import AmountDetails
import sms


@receiver(post_save, sender=AmountDetails)
def send_message(sender, instance, created, **kwargs):
    if instance.is_closed:
        message_to_broadcast = f"Thanks for paying loan amount, " \
                               f"you have borrowed {instance.amount} on {str(instance.start_date)}, " \
                               f"interest still date is {instance.interest_amount}"
        client = messagebird.Client("2u2iitntnzYlWhfiucKNY7g9S")
        message = client.message_create(
            'TestMessage',
            '+918185819879',
            message_to_broadcast,
            {'reference': 'Foobar'}
        )


client = messagebird.Client("EQNCurUYqAu9lhu7VNkwzwq5p")
message = client.message_create(
      '918185819879',
      '918185819879',
      'This is a test message',
      {'reference': 'Foobar'}
  )
# import urllib.request
# import urllib.parse


# @receiver(post_save, sender=AmountDetails)
# def send_sms(sender, instance, created, **kwargs):
#     if instance.is_closed:
#         number = instance.lender_mobile_number
#         message_to_broadcast = f"Thanks for paying loan amount, " \
#                                f"you have borrowed {instance.amount} on {str(instance.start_date)}, " \
#                                f"interest still date is {instance.interest_amount}"
#         data = urllib.parse.urlencode(
#             {
#                 'apikey': "Mzg1NDVhNmM3MDZlNjc0ZjZmNDY3MTU2Nzg1NzMwNGQ=",
#                 'numbers': '91' + str(number),
#                 'message': message_to_broadcast,
#                 'sender': "MARUTH"
#             }
#         )
#         data = data.encode('utf-8')
#         request = urllib.request.Request("https://api.textlocal.in/send/?")
#         f = urllib.request.urlopen(request, data)
#         fr = f.read()
#         print(fr)
