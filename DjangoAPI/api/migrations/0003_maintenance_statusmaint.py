# Generated by Django 4.0.6 on 2022-11-04 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_releasemachine_exama_releasemachine_examb_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenance',
            name='statusMaint',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
