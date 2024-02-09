# Generated by Django 3.2.5 on 2021-09-09 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmscontacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactinfolocalization',
            old_name='name',
            new_name='label',
        ),
        migrations.RemoveField(
            model_name='contactinfo',
            name='name',
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='label',
            field=models.CharField(blank=True, default='', max_length=160),
        ),
    ]