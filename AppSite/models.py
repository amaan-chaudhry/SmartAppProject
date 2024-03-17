from django.db import models
class User(AbstractUser):
    subscribe_newsletters = models.BooleanField(default=True)
    old_id = models.IntegerField(null=True, blank=True)
    old_source = models.CharField(max_length=25, null=True, blank=True)
