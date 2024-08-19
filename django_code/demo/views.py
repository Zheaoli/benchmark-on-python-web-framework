import random

from django.core import serializers
from django.shortcuts import HttpResponse

from .models import DemoData

TEMP = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"


# Create your views here.
def demo_views(request):
    demo=random.choices(TEMP, k=random.randrange(1, 254))
    DemoData.objects.create(
        name="".join(demo)
    )
    result = DemoData.objects.filter(
        name="".join(demo)
    )
    # x = json.dumps(request.body)
    return HttpResponse(
        serializers.serialize("json", result if result else []),
        content_type="application/json",
    )
