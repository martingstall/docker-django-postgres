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
        cf.name = "Campaign Framework Example 1"
        cf.save()

        phase = CampaignFrameworkPhase()
        phase.campaign_framework_id = cf.id
        phase.name = "Phase Example 1"
        phase.save()

        step = CampaignFrameworkStep()
        step.phase_id = phase.id
        step.name = "Bootstrap Step"
        step.html_layout = "bootstrap_step_example.html"
        step.save()

        step = CampaignFrameworkStep()
        step.phase_id = phase.id
        step.name = "CSS Grid Step"
        step.html_layout = "css_grid_step_example.html"
        step.save()

        step = CampaignFrameworkStep()
        step.phase_id = phase.id
        step.name = "JSON Step"
        step.html_layout = "json_step_example.html"
        step.save()

        return HttpResponse("Created")

    except Exception as e:
        return HttpResponse(e)


def update_example(request):
    """

    :param request:
    :type request:
    :return:
    :rtype:
    """
    json_layout = {
        "bootstrap_columns": [
            {
                "class": "col-sm-3",
                "field_type": "input",
                "input_type": "date",
                "name": "date_field_1",
                "label": "Date",
                "required": True
            },
            {
                "class": "col-sm-3",
                "field_type": "input",
                "input_type": "text",
                "name": "field_1",
                "label": "Text #1",
                "required": True,
                "placeholder": "Enter something"
            },
            {
                "class": "col-sm-3",
                "field_type": "input",
                "input_type": "number",
                "name": "field_2",
                "label": "Number Input #1",
                "required": True,
                "placeholder": "Only takes numbers",
                "tooltip": {
                    "title": "Lorum ipsum blah blah",
                    "placement": "top"
                }
            },
            {
                "class": "col-sm-3",
                "field_type": "select",
                "multiple": False,
                "name": "select_1",
                "label": "Select #1",
                "required": False,
                "options": [
                    {
                        "value": "lorum",
                        "label": "Lorum"
                    },
                    {
                        "value": "ipsum",
                        "label": "Ipsum"
                    }
                ]
            },
            {
                "class": "col-sm-3",
                "field_type": "radio",
                "multiple": False,
                "name": "radio_1",
                "label": "Radio #1",
                "required": False,
                "options": [
                    {
                        "value": "aaa",
                        "label": "These are A's"
                    },
                    {
                        "value": "bbb",
                        "label": "These are B's"
                    }
                ]
            },
            {
                "class": "col-sm-12",
                "field_type": "textarea",
                "name": "textarea_1",
                "label": "Textarea #1"
            }
        ]
    }
    step = CampaignFrameworkStep.objects.get(pk=5)
    step.json_layout = json_layout
    step.save()

    return HttpResponse("Updated")
