import uuid

from django.contrib.postgres.fields import JSONField
from django.db import models


class CampaignFramework(models.Model):
    id = models.AutoField("id", primary_key=True)
    name = models.CharField("Name", max_length=255, null=False, blank=False)

    class Meta:
        app_label = 'sample_app'
        db_table = 'campaign_frameworks'
        unique_together = (('name',),)


class CampaignFrameworkPhase(models.Model):
    id = models.AutoField("id", primary_key=True)
    campaign_framework = models.ForeignKey("CampaignFramework", on_delete=models.CASCADE)
    name = models.CharField("Name", max_length=255, null=False, blank=False)
    description = models.TextField("Description", null=True, blank=True)

    class Meta:
        app_label = 'sample_app'
        db_table = 'campaign_framework_phases'
        unique_together = (('campaign_framework', 'name'),)

    def __str__(self):
        return "%s" % self.name


class CampaignFrameworkStep(models.Model):
    id = models.AutoField("id", primary_key=True)
    phase = models.ForeignKey(
        "CampaignFrameworkPhase",
        verbose_name="Phase",
        on_delete=models.CASCADE
    )
    name = models.CharField("Step Name", max_length=255, null=False, blank=False)
    description = models.TextField("Description", null=True, blank=True)
    layout = models.CharField("HTML", max_length=255, null=False, blank=False)

    class Meta:
        app_label = 'sample_app'
        db_table = 'campaign_framework_steps'
        unique_together = (('phase', 'name'),)

    def __str__(self):
        return "%s" % self.name
