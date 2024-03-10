"""
Datbase tables.

User: Django default user model.

"""

from django.db import models


class Activity(models.Model):
    uid = models.CharField(max_length=255, primary_key=True)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=50)
    description_filter_html = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    web_sales = models.URLField(blank=True, null=True)
    source_web_promote = models.URLField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    edit_modify_date = models.DateTimeField()
    source_web_name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    hit_rate = models.IntegerField()


class Location(models.Model):
    location = models.CharField(max_length=255)
    location_name = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)


class ShowInfo(models.Model):
    activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE, related_name="show_infos"
    )
    time = models.DateTimeField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    on_sales = models.CharField(max_length=1)
    price = models.CharField(max_length=255, blank=True, null=True)
    end_time = models.DateTimeField()


class Unit(models.Model):
    unit_name = models.CharField(max_length=255)
    unit_type = models.CharField(max_length=50)


class UnitActivityLink(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
