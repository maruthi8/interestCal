from celery.schedules import crontab
from celery.task import periodic_task

from api.models import AmountDetails


@periodic_task(run_every=crontab(minute=1), queue='interest', options={'queue': 'interest'})
def update_interest_task():
    amounts = AmountDetails.objects.filter(is_closed=False)
    for amount in amounts:
        interest_percentage = amount.interest_percentage
        borrowed_amount = amount.amount

        interest = borrowed_amount * 1 * (round(interest_percentage / 36500, 4))
        amount.interest_amount += interest
        amount.save()
