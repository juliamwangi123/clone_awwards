# Generated by Django 4.0.5 on 2022-06-14 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_site_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='reviews',
            field=models.ManyToManyField(blank=True, null=True, to='api.review'),
        ),
    ]
