# Generated by Django 2.0.3 on 2018-04-01 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decision', '0005_auto_20180401_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='decision',
            name='text',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]