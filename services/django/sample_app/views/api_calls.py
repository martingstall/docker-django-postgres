import json
import requests

from cookies import Cookies, Cookie

from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from ..models.users import *
from ..data_connections.factory import Factory as DataConnFactory


def test_dc(request):
    """

    :param request:
    :type request:
    :return:
    :rtype:
    """
    payload = {
        "data_fields": "dsp_campaign_name,budget,alltime_metric_rollup.dsp_impressions",
        "office_market": 1,
        #"length": "all"
        "length": "200"
    }
    base_url = "https://www.accuenplatform.com/backstage/accuen_api/"
    url = base_url + "DSPCampaignDim"
    response = requests.get(
        url,
        params=payload,
        headers=get_digital_content_conn(request)
    )
    data = json.loads(response.text)

    return HttpResponse(
        json.dumps(data),
        content_type="application/json"
    )


def test_ae(request):
    """

    :param request:
    :type request:
    :return:
    :rtype:
    """
    #username = request.GET.get('username')
    #password = request.GET.get('password')
    username = "matt.artingstall@annalect.com"
    password = "Eng!n33r77"

    payload = {}
    base_url = "https://audience.annalect.com/api"
    # Working project id: 01c22232-76d6-11e9-8de8-0a10e129e67c
    project_id = request.GET.get('projectid', '01c22232-76d6-11e9-8de8-0a10e129e67c')
    # Working client id: 449203c6-7ed3-11e8-8b6b-0a35455287ac
    client_id = request.GET.get('clientid', '449203c6-7ed3-11e8-8b6b-0a35455287ac')
    #url = base_url + "/session/initial_metadata/dff361c4-5ad9-11e9-b6d9-0a30447703ec"
    #url = base_url + "/audience/audience_id_export/ac481ade-d56a-11e9-827d-12eb309feec0"
    #url = base_url + "/audience/history_build/ac481ade-d56a-11e9-827d-12eb309feec0"
    if project_id:
        url = base_url + f"/audience/list/{project_id}/{client_id}"
    else:
        url = base_url + f"/project/list/{client_id}"

    response = requests.get(
        url,
        params=payload,
        cookies=get_audience_explorer_conn(request, username, password)
    )
    print ("RESPONSE: ", response)
    print ("RESPONSE.TEXT: ", response.text)
    data = json.loads(response.text)

    return HttpResponse(
        json.dumps(data),
        content_type="application/json"
    )


def get_audience_explorer_conn(request, username, password):
    """

    :param request:
    :type request:
    :param username:
    :type username:
    :param password:
    :type password:
    :return:
    :rtype:
    """
    if 'xxx_ANsid' in request.session and request.session['ANsid']:
        print ("")
        print ("")
        print ("request.session['ANsid']: ", request.session['ANsid'])
        print ("")
        print ("")
        auth = {
            'ANsid': request.session['ANsid']
        }
    else:
        url = "https://access.annalect.com/am/amapi/user/login/" + str(username)
        r = requests.post(
            url,
            data={
                "p": password
            },
            timeout=15.0,
            verify=False
        )
        print ("get_audience_explorer_conn > response", r)
        response = json.loads(r.content)
        request.session['ANsid'] = response.get('sid')
        auth = {
            'ANsid': response.get('sid')
        }

    return auth


def get_digital_content_conn(request):
    """

    :param request:
    :type request:
    :return:
    :rtype:
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Token 627c549329ec054447a9c67793ba1f3b1b5332ae"
    }

    return headers


def normalization_example(request):
    """

    :param request:
    :type request:
    :return:
    :rtype:
    """
    data = {}
    app_data = {}
    data_conn_system_key = None
    app = None

    if request.GET.get('which') == "dc":
        data_conn_system_key = "digital_content"

        app = {
             "data_connection":{
                "id":1,
                "url":"https://www.accuenplatform.com/backstage/accuen_api/DSPCampaignDim",
                "params":{
                   "data_fields":"dsp_campaign_name,budget,alltime_metric_rollup.dsp_impressions",
                   "length":"20"
                },
                "filters":[
                   {
                      "label":"Advertiser",
                      "select":"single",
                      "param":"advertiser_id",
                      "input_value":"omg_advertiser_id",
                      "input_label":"omg_advertiser_name",
                      "endpoint":"http://www.accuenplatform.com/backstage/accuen_api/OMGAdvertiser/?data_fields=omg_advertiser_name&order_by=omg_advertiser_name&order_dir=asc&length=all"
                   }
                ]
             },
             "inject_id":1589991382628,
             "module_title":"DC Table Example",
             "columns":[
                {
                   "label":"Campaign Name",
                   "data":"dsp_campaign_name",
                   "format":"text"
                },
                {
                   "label":"Budget",
                   "data":"budget",
                   "format":"currency"
                },
                {
                   "label":"Omnet",
                   "data":"is_omnet",
                   "format":"text"
                },
                {
                   "label":"DSP Impressions",
                   "data":"alltime_metric_rollup.dsp_impressions",
                   "format":"digits"
                }
             ],
             "type":"table"
        }
        response = requests.get(
            app.get('data_connection').get('url'),
            params=app.get('data_connection').get('params'),
            headers=get_digital_content_conn(request)
        )
        app_data = json.loads(response.text)

    elif request.GET.get('which') == "ae":
        data_conn_system_key = "audience_explorer"
        app = {
             "data_connection":{
                "id":2,
                "url":"https://audience.annalect.com/api/session/initial_metadata/{guid_client}",
                "params":{

                },
                "filters":[

                ]
             },
             "inject_id":123456789,
             "module_title":"AE Table Example",
             "columns":[
                {
                   "label":"Audience Name",
                   "data":"audience_name",
                   "format":"text"
                },
                {
                   "label":"Client Name",
                   "data":"person_update",
                   "format":"text"
                },
                {
                   "label":"Last Accessed",
                   "data":"data_environment_name",
                   "format":"text"
                }
             ],
             "type":"table"
        }

        username = "matt.artingstall@annalect.com"
        password = "Eng!n33r77"
        base_url = "https://audience.annalect.com/api"
        #url = base_url + "/session/initial_metadata/dff361c4-5ad9-11e9-b6d9-0a30447703ec"
        url = base_url + "/audience/list/01c22232-76d6-11e9-8de8-0a10e129e67c/449203c6-7ed3-11e8-8b6b-0a35455287ac"
        response = requests.get(
            url,
            cookies=get_audience_explorer_conn(request, username, password)
        )
        print("RESPONSE: ", response.status_code)
        app_data = json.loads(response.text)
        #app_data = raw_app_data.get('user_profile').get('clients')

    DataClass = DataConnFactory.getDataClass(data_conn_system_key)
    dataClass = DataClass()
    data = dataClass.normalize_table_data(app, app_data)

    #template = loader.get_template("sample_app/normalization_example.html")
    #return HttpResponse(template.render(data, request))
    return HttpResponse(
        json.dumps(data),
        content_type="application/json"
    )
