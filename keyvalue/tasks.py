import datetime
from django.utils import timezone
from background_task import background
from .models import KeyValue

# just checking


@background(schedule=320)
def time_to_live(key):
    obj = KeyValue.objects.get(key=key)
    data = obj.timestamp
    print(data)
    current_time = timezone.now()
    try:
        if current_time > obj.timestamp:
            obj.value = 'null'
            obj.save()
    except:
        print("error")