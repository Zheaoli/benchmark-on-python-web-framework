from django.db import models

# Create your models here.


class DemoData(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, null=False)
    name = models.CharField(null=False, max_length=255)
    create_time = models.DateTimeField(null=False)
    update_time = models.DateTimeField(null=False)

    class Meta:
        db_table = "demo_data"
