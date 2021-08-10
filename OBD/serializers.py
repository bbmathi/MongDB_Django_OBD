from rest_framework import serializers 
from OBD.models import Obd
 
 
class ObdSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Obd
        fields = ('id',
                  'OrgID',
                  'SiteID',
                  'VOB_ID',
                  'OBD_TAG_ID',
                  'IMEI',
                  'Latitude',
                  'North_South',
                  'Longitude',
                  'East_West',
                  'Signal_Strength',
                  'timeout',
                  'Device_Status',
                  'Internal_Battery_Level',)
