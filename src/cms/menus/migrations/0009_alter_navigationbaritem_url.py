# Generated by Django 3.2.3 on 2021-06-14 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsmenus', '0008_alter_navigationbaritem_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navigationbaritem',
            name='url',
            field=models.CharField(blank=True, default='', help_text='url', max_length=2048),
        ),
    ]