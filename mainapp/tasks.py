from celery import shared_task
from django.http.response import HttpResponse
import  time
@shared_task(bind=True)
def test_func(self):
    #operations
    time.sleep(10)
    return HttpResponse("Done")