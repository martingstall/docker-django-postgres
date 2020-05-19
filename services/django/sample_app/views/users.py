import time
import datetime

from django.shortcuts import render
from django.http import HttpResponse

from ..models.users import *


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def create_perms(request):
    PermsUUIDField.objects.bulk_create(
        [
            PermsUUIDField(label="Admin"),
            PermsUUIDField(label="Editor"),
            PermsUUIDField(label="User"),
        ]
    )

    PermsAutoField.objects.bulk_create(
        [
            PermsAutoField(label="Admin"),
            PermsAutoField(label="Editor"),
            PermsAutoField(label="User"),
        ]
    )
    return HttpResponse("Perms created")


def create_users(request):
    user = UserUUIDField()
    user.first_name = "Matt UUID"
    user.save()

    user.perms_uuid_field.add(*PermsUUIDField.objects.all())

    article = ArticleUUIDField()
    article.name = "Article 1 UUID"
    article.user_uuid_field = user
    article.save()

    article = ArticleUUIDField()
    article.name = "Article 2 UUID"
    article.user_uuid_field = user
    article.save()

    """ ********************** """

    user = UserAutoField()
    user.first_name = "Matt AutoField"
    user.save()

    user.perms_auto_field.add(*PermsAutoField.objects.all())

    article = ArticleAutoField()
    article.name = "Article 1 AutoField"
    article.user_auto_field = user
    article.save()

    article = ArticleAutoField()
    article.name = "Article 2 AutoField"
    article.user_auto_field = user
    article.save()

    return HttpResponse("Users created")


def list_users(request):
    x = ArticleUUIDField.objects.filter(user_uuid_field__first_name__icontains="matt")
    print (x.query)

    x = ArticleAutoField.objects.filter(user_auto_field__first_name__icontains="matt")
    print(x.query)

    print (time.time())
    for x in UserUUIDField.objects.all():
        print (x.first_name)
        for art in ArticleUUIDField.objects.filter(user_uuid_field=x):
            print(art.name)
    print(time.time())

    print(time.time())
    for x in UserAutoField.objects.all():
        print(x.first_name)
        for art in ArticleAutoField.objects.filter(user_auto_field=x):
            print(art.name)
    print(time.time())

    return HttpResponse("Hello, world. You're at the polls index.")
