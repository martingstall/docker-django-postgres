import json
import time
import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader

from ..models.campaign import *
from ..models.campaign_framework import *


def create_example(request):
    """

    :param request:
    :type request:
    :return:
    :rtype:
    """
    try:
        campaign = Campaign()
        campaign.campaign_framework_id = 1
        campaign.name = "Campaign Example 1"
        campaign.save()

        campaign_step_data = CampaignStepData()
        campaign_step_data.campaign_id = campaign.id
        campaign_step_data.campaign_framework_step_id = 1
        campaign_step_data.save()

        campaign_step_data = CampaignStepData()
        campaign_step_data.campaign_id = campaign.id
        campaign_step_data.campaign_framework_step_id = 2
        campaign_step_data.save()

        return HttpResponse("Created")

    except Exception as e:
        return HttpResponse(e)


def view_step(request, campaign_id, cf_step_id):
    """

    :param request:
    :type request:
    :param campaign_id:
    :type campaign_id:
    :param cf_step_id:
    :type cf_step_id:
    :return:
    :rtype:
    """
    campaign = Campaign.objects.get(pk=campaign_id)
    cf_step = CampaignFrameworkStep.objects.get(
        pk=cf_step_id
    )
    campaign_step = CampaignStepData.objects.get(
        campaign_id=campaign.id,
        campaign_framework_step_id=cf_step.id
    )
    campaign_step_data = campaign_step.campaign_step_data
    #print ("campaign_step_data.get('app_1'): " , campaign_step_data.get('app_1'))

    data = {
        "campaign": campaign,
        "cf_step": cf_step,
        "campaign_step_data": json.dumps(campaign_step_data),
        "which_normalization_example": campaign_step_data.get('app_1')
    }
    template = loader.get_template("sample_app/" + cf_step.layout)
    return HttpResponse(template.render(data, request))


def save_step_data(request, campaign_id, cf_step_id):
    """

    :param request:
    :type request:
    :param campaign_id:
    :type campaign_id:
    :param cf_step_id:
    :type cf_step_id:
    :return:
    :rtype:
    """
    data = {
        "status": "success"
    }
    try:
        raw = json.dumps(request.POST)
        clean = json.loads(raw)
        clean.pop('csrfmiddlewaretoken', None)
        print ("")
        print ("")
        print (clean)
        print ("")
        print ("")

        step = CampaignStepData.objects.get(
            campaign_id=campaign_id,
            campaign_framework_step_id=cf_step_id
        )
        step.campaign_step_data = clean
        step.save()

    except Exception as e:
        data = {
            "status": "fail",
            "reason": str(e)
        }

    return HttpResponse(
        json.dumps(data),
        content_type="application/json"
    )


def lit_table_example(request):
    """

    :param request:
    :type request:
    :return:
    :rtype:
    """
    data = {

    }
    template = loader.get_template("sample_app/lit_table_example.html")
    return HttpResponse(template.render(data, request))
