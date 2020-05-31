import json
import time
import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt

from pptx import Presentation
from pptx.util import Inches

from ..models.campaign import *
from ..models.campaign_framework import *


def campaign_details(request, campaign_id):
    """

    :param request:
    :type request:
    :param campaign_id:
    :type campaign_id:
    :return:
    :rtype:
    """
    campaign = Campaign.objects.get(pk=campaign_id)
    steps = CampaignFrameworkStep.objects.filter(
        phase_id__in=CampaignFrameworkPhase.objects.filter(
            campaign_framework_id = campaign.campaign_framework_id
        )
    )

    data = {
        "campaign": campaign,
        "steps": steps
    }
    template = loader.get_template("sample_app/campaign_detail.html")
    return HttpResponse(template.render(data, request))


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

    data = {
        "campaign": campaign,
        "cf_step": cf_step,
        "json_layout": json.dumps(cf_step.json_layout),
        "campaign_step_data": json.dumps(campaign_step_data),
        "which_normalization_example": campaign_step_data.get('app_1')
    }
    template = loader.get_template("sample_app/" + cf_step.html_layout)
    return HttpResponse(template.render(data, request))


@csrf_exempt
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
        form_data = json.dumps(request.POST)
        step = CampaignStepData.objects.get(
            campaign_id=campaign_id,
            campaign_framework_step_id=cf_step_id
        )
        step.campaign_step_data = json.loads(form_data)
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


def create_campaign_pptx(request, campaign_id):
    """

    :param request:
    :type request:
    :param campaign_id:
    :type campaign_id:
    :return:
    :rtype:
    """
    campaign = Campaign.objects.get(pk=campaign_id)
    cf_steps = CampaignFrameworkStep.objects.filter(
        phase_id__in=CampaignFrameworkPhase.objects.filter(
            campaign_framework_id=campaign.campaign_framework_id
        )
    )

    filename = "OmniTemplateTest.pptx"
    prs = Presentation(filename)

    intro_slide = prs.slides.get(prs.slides[0].slide_id)
    intro_slide.shapes.title.text = campaign.name
    intro_slide.placeholders[1].text = "Campaign description here..."

    slide_template = prs.slide_layouts[8]
    for cf_step in cf_steps:
        slide = prs.slides.add_slide(slide_template)
        slide.shapes.title.text = cf_step.name

        campaign_step = CampaignStepData.objects.get(
            campaign_id=campaign.id,
            campaign_framework_step_id=cf_step.id
        )
        campaign_step_data = campaign_step.campaign_step_data

        top = 1.5
        height = 1
        for row in cf_step.json_layout.get('rows'):
            left = 0.5
            for col in row.get('columns'):
                try:
                    width = int(col.get('class').replace('col-sm-', ''))
                except Exception as e:
                    print ("Couldn't determine width: ", e)
                    width = 1
                label = col.get('label')
                value = campaign_step_data[col.get('name')]
                text_box = slide.shapes.add_textbox(
                    Inches(left),
                    Inches(top),
                    Inches(width),
                    Inches(height)
                )
                text_box.text_frame.text = label + ": " + str(value)
                left = left + width

            top = top + 0.5

    prs.save(campaign.name + ".pptx")

    return HttpResponse("Created")


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
