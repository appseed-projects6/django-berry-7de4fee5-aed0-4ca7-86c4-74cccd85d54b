# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Usertype(models.Model):

    #__Usertype_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Usertype_FIELDS__END

    class Meta:
        verbose_name        = _("Usertype")
        verbose_name_plural = _("Usertype")


class Accountmaster(models.Model):

    #__Accountmaster_FIELDS__

    #__Accountmaster_FIELDS__END

    class Meta:
        verbose_name        = _("Accountmaster")
        verbose_name_plural = _("Accountmaster")


class Projecttype(models.Model):

    #__Projecttype_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Projecttype_FIELDS__END

    class Meta:
        verbose_name        = _("Projecttype")
        verbose_name_plural = _("Projecttype")


class Project(models.Model):

    #__Project_FIELDS__
    code = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    init_date = models.CharField(max_length=255, null=True, blank=True)
    end_date = models.CharField(max_length=255, null=True, blank=True)
    project_type_id = models.CharField(max_length=255, null=True, blank=True)

    #__Project_FIELDS__END

    class Meta:
        verbose_name        = _("Project")
        verbose_name_plural = _("Project")


class Accountdetail(models.Model):

    #__Accountdetail_FIELDS__
    description = models.CharField(max_length=255, null=True, blank=True)

    #__Accountdetail_FIELDS__END

    class Meta:
        verbose_name        = _("Accountdetail")
        verbose_name_plural = _("Accountdetail")



#__MODELS__END
