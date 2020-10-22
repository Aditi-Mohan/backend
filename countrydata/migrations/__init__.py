import time
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from ..models import Sentdate, initialize
from ..functions import send_email_to_sub

scheduler = BackgroundScheduler()
scheduler.start()

def update_scheduler():
    scheduler.add_job(schedule, 'date', run_date=datetime.now()+timedelta(days=1))
    date = Sentdate.objects.all()[0]
    date.date = datetime.now().strftime(f"%d-%m-%Y")
    date.save()



def schedule():
    initialize()
    send_email_to_sub()
    update_scheduler()

date = Sentdate.objects.all()[0]
date_object = datetime.strptime(date.date, f'%d-%m-%Y').date()
print(date.date)
if date_object == datetime.now().date():
    pass
else:
    schedule()
    date.date = datetime.now().strftime(f"%d-%m-%Y")
    date.save()
    print(Sentdate.objects.all()[0].date)
