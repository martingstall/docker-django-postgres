import uuid
from django.db import models


class UserUUIDField(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.TextField("First Name", max_length=255, blank=False)
    perms_uuid_field = models.ManyToManyField("PermsUUIDField", verbose_name="Permissions")

    class Meta:
        app_label = "sample_app"
        db_table = "user_uuid_field"


class PermsUUIDField(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = models.TextField("Perm Label", max_length=255, blank=False)

    class Meta:
        app_label = "sample_app"
        db_table = "perms_uuid_field"


class ArticleUUIDField(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField("Perm Label", max_length=255, blank=False)
    user_uuid_field = models.ForeignKey("UserUUIDField", verbose_name="User", on_delete=models.CASCADE)

    class Meta:
        app_label = "sample_app"
        db_table = "articles_uuid_field"


class UserAutoField(models.Model):
    id = models.AutoField("ID", primary_key=True)
    first_name = models.TextField("First Name", max_length=255, blank=False)
    perms_auto_field = models.ManyToManyField("PermsAutoField", verbose_name="Permissions")

    class Meta:
        app_label = "sample_app"
        db_table = "user_auto_field"


class PermsAutoField(models.Model):
    id = models.AutoField("ID", primary_key=True)
    label = models.TextField("Perm Label", max_length=255, blank=False)

    class Meta:
        app_label = "sample_app"
        db_table = "perms_auto_field"


class ArticleAutoField(models.Model):
    id = models.AutoField("ID", primary_key=True)
    name = models.TextField("Perm Label", max_length=255, blank=False)
    user_auto_field = models.ForeignKey("UserAutoField", verbose_name="User", on_delete=models.CASCADE)

    class Meta:
        app_label = "sample_app"
        db_table = "articles_auto_field"
