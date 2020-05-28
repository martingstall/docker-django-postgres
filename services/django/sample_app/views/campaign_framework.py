import time
import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader

from ..models.campaign_framework import *


def create_example(request):
    """

    :param request:
    :type request:
    :return:
    :rtype:
    """
    try:
        cf = CampaignFramework()
        cf.name = "Example 1"
        cf.save()

        phase = CampaignFrameworkPhase()
        phase.campaign_framework_id = cf.id
        phase.name = "Lorum Phase"
        phase.save()

        step = CampaignFrameworkStep()
        step.phase_id = phase.id
        step.name = "Ipsum Step"
        step.layout = "ipsum_step_example.html"
        step.save()

        step = CampaignFrameworkStep()
        step.phase_id = phase.id
        step.name = "Lorum Step"
        step.layout = "lorum_step_example.html"
        step.save()

        return HttpResponse("Created")

    except Exception as e:
        return HttpResponse(e)
