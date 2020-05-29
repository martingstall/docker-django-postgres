import uuid

from django.contrib.postgres.fields import JSONField
from django.db import models


class Campaign(models.Model):
    id = models.AutoField("id", primary_key=True)
    campaign_framework = models.ForeignKey(
        "CampaignFramework",
        verbose_name="Campaign Framework",
        on_delete=models.CASCADE
    )
    name = models.CharField("Campaign Name", max_length=255, null=False, blank=False)

    class Meta:
        app_label = 'sample_app'
        db_table = 'campaigns'
        unique_together = (('campaign_framework','name'),)

    def __str__(self):
        return "%s" % self.name


class CampaignStepData(models.Model):
    id = models.AutoField("id", primary_key=True)
    campaign = models.ForeignKey(
        "Campaign",
        verbose_name="Campaign",
        on_delete=models.CASCADE
    )
    campaign_framework_step = models.ForeignKey(
        "CampaignFrameworkStep",
        verbose_name="CF Step",
        on_delete=models.CASCADE
    )
    campaign_step_data = JSONField("Campaign Step Data", default=dict)

    class Meta:
        app_label = 'sample_app'
        db_table = 'campaign_step_data'
        unique_together = (('campaign','campaign_framework_step'),)
