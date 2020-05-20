import json
import requests

from cookies import Cookies, Cookie

from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from ..models.users import *


def test_dc(request):
    """

    :param request:
    :type request:
    :return:
    :rtype:
    """
    payload = {}
    base_url = "https://www.accuenplatform.com/backstage/accuen_api/"
    url = base_url + "OMGAdvertiser"
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
    url = base_url + "/session/initial_metadata/dff361c4-5ad9-11e9-b6d9-0a30447703ec"
    #url = base_url + "/audience/list/f29ec394-df96-11e4-ad98-121cf53dff64/ac425072-d56a-11e9-827d-12eb309feec0"
    #url = base_url + "audience/audience_id_export/ac481ade-d56a-11e9-827d-12eb309feec0"
    response = requests.get(
        url,
        params=payload,
        cookies=get_audience_explorer_conn(request, username, password)
    )
    print (response.text)
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
    if 'ANsid' in request.session and request.session['ANsid']:
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


def web_component(request):
    """

    :param request:
    :type request:
    :return:
    :rtype:
    """
    data = {

    }
    template = loader.get_template("sample_app/table.html")
    return HttpResponse(template.render(data, request))
