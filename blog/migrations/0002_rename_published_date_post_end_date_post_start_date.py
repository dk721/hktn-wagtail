# Generated by Django 4.1.7 on 2023-04-01 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='published_date',
            new_name='end_date',
        ),
        migrations.AddField(
            model_name='post',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
