import json
import time
import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader

from ..models.app_store import *


def create_example(request):
    """

    :param request:
    :type request:
    :return:
    :rtype:
    """
    data_structure_example = {
        "data_connection": {
            "id": 1,
            "url": "https://www.accuenplatform.com/backstage/accuen_api/DSPCampaignDim",
            "params": {
                "data_fields": "dsp_campaign_name,budget,alltime_metric_rollup.dsp_impressions",
                "length": "20"
            },
            "filters": [
                {
                    "label": "Advertiser",
                    "select": "single",
                    "param": "advertiser_id",
                    "input_value": "omg_advertiser_id",
                    "input_label": "omg_advertiser_name",
                    "endpoint": "http://www.accuenplatform.com/backstage/accuen_api/OMGAdvertiser/?data_fields=omg_advertiser_name&order_by=omg_advertiser_name&order_dir=asc&length=all"
                }
            ]
        },
        "inject_id": 1589991382628,
        "module_title": "DC Table Example",
        "columns": [
            {
                "label": "Campaign Name",
                "data": "dsp_campaign_name",
                "format": "text"
            },
            {
                "label": "Budget",
                "data": "budget",
                "format": "currency"
            },
            {
                "label": "Omnet",
                "data": "is_omnet",
                "format": "text"
            },
            {
                "label": "DSP Impressions",
                "data": "alltime_metric_rollup.dsp_impressions",
                "format": "digits"
            }
        ],
        "type": "table"
    }
    try:
        app = App()
        app.app_name = "Test Table"
        app.app_desc = "Lorum ipsum"
        app.data_structure = data_structure_example
        app.display_structure = "lit_table_example.html"
        app.save()

        return HttpResponse("Created")

    except Exception as e:
        return HttpResponse(e)


def load_app(request, app_id):
    """

    :param request:
    :type request:
    :param app_id:
    :type app_id:
    :return:
    :rtype:
    """
    app = App.objects.get(pk=app_id)
    print (app.data_structure)

    return HttpResponse("APP")
