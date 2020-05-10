import random

from django.core import serializers
from django.shortcuts import HttpResponse

from .models import DemoData

TEMP = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"


# Create your views here.
def demo_views(request):
    result = DemoData.objects.filter(
        name="".join(random.choices(TEMP, k=random.randrange(1, 254)))
    )
    # x = json.dumps(request.body)
    return HttpResponse(
        serializers.serialize("json", result.values() if result else []),
        content_type="application/json",
    )
