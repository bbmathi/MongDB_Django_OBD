from django.db import models


class Obd(models.Model):
    OrgID=models.CharField(max_length=70, blank=False, default='')
    SiteID=models.CharField(max_length=70, blank=False, default='')
    VOB_ID=models.CharField(max_length=70, blank=False, default='')
    OBD_TAG_ID=models.CharField(max_length=70, blank=False, default='')
    IMEI=models.CharField(max_length=70, blank=False, default='')
    Latitude=models.CharField(max_length=70, blank=False, default='')
    North_South=models.CharField(max_length=70, blank=False, default='')
    Longitude=models.CharField(max_length=70, blank=False, default='')
    East_West=models.CharField(max_length=70, blank=False, default='')
    Signal_Strength = models.CharField(max_length=70, blank=False, default='')
    timeout = models.CharField(max_length=70, blank=False, default='')
    Device_Status = models.CharField(max_length=70, blank=False, default='')
    Rpm = models.CharField(max_length=70, blank=False, default='')
    Internal_Battery_Level = models.CharField(max_length=70, blank=False, default='')



