from django.conf import settings
from django.db import models
class BoxStatuses(models.Model):
    'Generated Model'
    statusId = models.UUIDField()
    statusName = models.TextField()
class Locations(models.Model):
    'Generated Model'
    locationId = models.UUIDField()
    locationName = models.TextField()
class Boxes(models.Model):
    'Generated Model'
    boxId = models.UUIDField()
    boxStatus = models.ForeignKey("home.BoxStatuses",on_delete=models.CASCADE,related_name="boxes_boxStatus",)
    boxLocation = models.ForeignKey("home.Locations",on_delete=models.CASCADE,null=True,blank=True,related_name="boxes_boxLocation",)
