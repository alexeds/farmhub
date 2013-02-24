from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class Business(models.Model):
    BUSINESS_TYPE_CHOICES = (
        ('retail', 'Retail'),
        ('restaurant', 'Restaurant'),
    )

    name = models.CharField(_('Name'), max_length=200)
    address = models.CharField(_('Address'), max_length=200)
    city = models.CharField(_('City'), max_length=100)
    state = models.CharField(_('State'), max_length=20)
    zip = models.IntegerField(_('ZIP Code'), max_length=9)
    type = models.CharField(_('Type of Business'), max_length=100, choices=BUSINESS_TYPE_CHOICES)
    percent_local = models.IntegerField(_('Percent of food that is locally sourced'), max_length=3, blank=True, null=True)
    items_available = models.CharField(_('Local Items Available'), max_length=500, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='/media/businesses')
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    
    creator = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_related")
    create_dt = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True, auto_now_add=True)
    
    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ("business.detail", [self.pk])