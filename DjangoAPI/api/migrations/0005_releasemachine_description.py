# Generated by Django 4.0.6 on 2022-11-14 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_maintenance_statusmaint'),
    ]

    operations = [
        migrations.AddField(
            model_name='releasemachine',
            name='description',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
    ]
