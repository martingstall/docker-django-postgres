import uuid

from django.contrib.postgres.fields import JSONField
from django.db import models


class App(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    app_name = models.CharField("App Name", max_length=255, null=False, blank=False)
    app_desc = models.CharField("App Description", max_length=255, null=False, blank=False)
    data_structure = JSONField("Data Structure", default=dict, null=True, blank=True)
    display_structure = models.TextField("Display Structure", null=True, blank=True)

    class Meta:
        app_label = 'sample_app'
        db_table = 'apps'
        unique_together = (('app_name',),)

    def __str__(self):
        return "%s" % self.app_name
