from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(_('Title'), max_length=200)
    address = models.CharField(_('Address'), max_length=200)
    city = models.CharField(_('City'), max_length=100)
    state = models.CharField(_('State'), max_length=20)
    zip = models.IntegerField(_('ZIP Code'), max_length=9)
    type = models.ForeignKey('Type')
    description = models.TextField(_('Description'), blank=True, null=True)
    contact = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_related_contact")
    website = models.URLField(_('Website'), max_length=200)
    
    creator = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_related_creator")
    create_dt = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True, auto_now_add=True)
    
    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ("event.detail", [self.pk])

class Type(models.Model):
    title = models.CharField(_('Title'), max_length=200)