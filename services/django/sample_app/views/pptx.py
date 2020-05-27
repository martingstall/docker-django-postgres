import json
import time
import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader

from pptx import Presentation


def index(request):
    """

    :param request:
    :type request:
    :return:
    :rtype:
    """
    data = {}
    template = loader.get_template("sample_app/save_pptx.html")
    return HttpResponse(template.render(data, request))


def save_pptx(request):
    """

    :param request:
    :type request:
    :return:
    :rtype:
    """
    prs = Presentation()
    title_slide_layout = prs.slide_layouts[0]
    slide = prs.slides.add_slide(title_slide_layout)
    title = slide.shapes.title
    subtitle = slide.placeholders[1]

    title.text = "Hello, World!"
    subtitle.text = "python-pptx was here!"

    prs.save('test.pptx')

    data = {}
    return HttpResponse(
        json.dumps(data),
        content_type="application/json"
    )
