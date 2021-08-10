# Generated by Django 3.2.6 on 2021-08-10 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0003_auto_20210810_0726'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutorial',
            old_name='title',
            new_name='Device_Status',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='description',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='published',
        ),
        migrations.AddField(
            model_name='tutorial',
            name='East_West',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='IMEI',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='Internal_Battery_Level',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='Latitude',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='Longitude',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='North_South',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='OBD_TAG_ID',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='OrgID',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='Signal_Strength',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='SiteID',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='VOB_ID',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='timeout',
            field=models.CharField(default='', max_length=70),
        ),
    ]