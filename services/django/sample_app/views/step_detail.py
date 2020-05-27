import time
import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader


def view_step(request):
    """

    :param request:
    :type request:
    :return:
    :rtype:
    """
    data = {

    }
    template = loader.get_template("sample_app/step_detail_2.html")
    return HttpResponse(template.render(data, request))
