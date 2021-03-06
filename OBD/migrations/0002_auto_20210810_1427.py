# Generated by Django 3.2.6 on 2021-08-10 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OBD', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Obd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrgID', models.CharField(default='', max_length=70)),
                ('SiteID', models.CharField(default='', max_length=70)),
                ('VOB_ID', models.CharField(default='', max_length=70)),
                ('OBD_TAG_ID', models.CharField(default='', max_length=70)),
                ('IMEI', models.CharField(default='', max_length=70)),
                ('Latitude', models.CharField(default='', max_length=70)),
                ('North_South', models.CharField(default='', max_length=70)),
                ('Longitude', models.CharField(default='', max_length=70)),
                ('East_West', models.CharField(default='', max_length=70)),
                ('Signal_Strength', models.CharField(default='', max_length=70)),
                ('timeout', models.CharField(default='', max_length=70)),
                ('Device_Status', models.CharField(default='', max_length=70)),
                ('Internal_Battery_Level', models.CharField(default='', max_length=70)),
            ],
        ),
        migrations.DeleteModel(
            name='Tutorial',
        ),
    ]
