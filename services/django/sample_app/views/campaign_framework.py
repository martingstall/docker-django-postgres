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
        cf = CampaignFramework()
        cf.name = "Campaign Framework Example 2"
        cf.save()

        campaign = Campaign()
        campaign.campaign_framework_id = cf.id
        campaign.name = "Campaign Example 2"
        campaign.save()

        phase = CampaignFrameworkPhase()
        phase.campaign_framework_id = cf.id
        phase.name = "Phase Example 1"
        phase.order = 1
        phase.save()

        step = CampaignFrameworkStep()
        step.phase_id = phase.id
        step.name = "Lorem ipsum dolor"
        step.order = 1
        step.html_layout = "json_step_example.html"
        step.save()

        campaign_step_data = CampaignStepData()
        campaign_step_data.campaign_id = campaign.id
        campaign_step_data.campaign_framework_step_id = step.id
        campaign_step_data.save()

        step = CampaignFrameworkStep()
        step.phase_id = phase.id
        step.name = "Excepteur sint occaecat"
        step.order = 2
        step.html_layout = "json_step_example.html"
        step.save()

        campaign_step_data = CampaignStepData()
        campaign_step_data.campaign_id = campaign.id
        campaign_step_data.campaign_framework_step_id = step.id
        campaign_step_data.save()

        step = CampaignFrameworkStep()
        step.phase_id = phase.id
        step.name = "Officia deserunt mollit"
        step.order = 3
        step.html_layout = "json_step_example.html"
        step.save()

        campaign_step_data = CampaignStepData()
        campaign_step_data.campaign_id = campaign.id
        campaign_step_data.campaign_framework_step_id = step.id
        campaign_step_data.save()

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
        "rows": [
            {
                "columns": [
                    {
                        "class": "col-sm-4",
                        "field_type": "input",
                        "input_type": "date",
                        "name": "date_field_1",
                        "label": "Date",
                        "required": True
                    },
                    {
                        "class": "col-sm-4",
                        "field_type": "input",
                        "input_type": "text",
                        "name": "field_1",
                        "label": "Text #1",
                        "required": True,
                        "placeholder": "Enter something"
                    },
                    {
                        "class": "col-sm-4",
                        "field_type": "input",
                        "input_type": "number",
                        "name": "field_2",
                        "label": "Number #1",
                        "required": True,
                        "placeholder": "Only takes numbers",
                        "tooltip": {
                            "title": "Lorum ipsum blah blah",
                            "placement": "top"
                        }
                    }
                ]
            },
            {
                "columns": [

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
                        "class": "col-sm-6",
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
                    }
                ]
            },
            {
                "columns": [
                    {
                        "class": "col-sm-12",
                        "field_type": "textarea",
                        "name": "textarea_1",
                        "label": "Textarea #1"
                    }
                ]
            }
        ]
    }

    json_layoutsfsa = {
        "rows": [
            {
                "columns": [
                    {
                        "class": "col-sm-4",
                        "field_type": "textarea",
                        "name": "textarea_1",
                        "label": "Textarea #1"
                    },
                    {
                        "class": "col-sm-4",
                        "field_type": "textarea",
                        "name": "textarea_2",
                        "label": "Textarea #2"
                    },
                    {
                        "class": "col-sm-4",
                        "field_type": "textarea",
                        "name": "textarea_3",
                        "label": "Textarea #3"
                    }
                ]
            }
        ]
    }

    json_layoutasdsa = {
        "rows": [
            {
                "columns": [
                    {
                        "class": "col-sm-2",
                        "field_type": "radio",
                        "multiple": False,
                        "name": "yesno_1",
                        "label": "Decision",
                        "label_position": "top",
                        "required": False,
                        "options": [
                            {
                                "value": "yes",
                                "label": "Yes"
                            },
                            {
                                "value": "no",
                                "label": "No"
                            },
                            {
                                "value": "maybe",
                                "label": "Maybe"
                            }
                        ]
                    },
                    {
                        "class": "col-sm-5",
                        "field_type": "input",
                        "input_type": "text",
                        "name": "size_1",
                        "label": "Size",
                        "label_position": "top",
                        "required": True,
                        "placeholder": "Enter Text Here"
                    },
                    {
                        "class": "col-sm-5",
                        "field_type": "input",
                        "input_type": "text",
                        "name": "definition_1",
                        "label": "Definition",
                        "label_position": "top",
                        "required": True,
                        "placeholder": "Enter Text Here"
                    }
                ]
            },
            {
                "columns": [
                    {
                        "class": "col-sm-2",
                        "field_type": "radio",
                        "multiple": False,
                        "name": "yesno_2",
                        "label": "Decision",
                        "label_position": "top",
                        "required": False,
                        "options": [
                            {
                                "value": "yes",
                                "label": "Yes"
                            },
                            {
                                "value": "no",
                                "label": "No"
                            },
                            {
                                "value": "maybe",
                                "label": "Maybe"
                            }
                        ]
                    },
                    {
                        "class": "col-sm-5",
                        "field_type": "input",
                        "input_type": "text",
                        "name": "size_2",
                        "label": "Size",
                        "label_position": "top",
                        "required": True,
                        "placeholder": "Enter Text Here"
                    },
                    {
                        "class": "col-sm-5",
                        "field_type": "input",
                        "input_type": "text",
                        "name": "definition_2",
                        "label": "Definition",
                        "label_position": "top",
                        "required": True,
                        "placeholder": "Enter Text Here"
                    }
                ]
            }
        ]
    }

    step = CampaignFrameworkStep.objects.get(pk=request.GET.get('id'))
    step.json_layout = json_layout
    step.save()

    return HttpResponse("Updated")
