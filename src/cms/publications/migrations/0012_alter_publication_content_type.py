# Generated by Django 3.2 on 2021-04-20 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmspublications', '0011_publication_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='content_type',
            field=models.CharField(choices=[('markdown', 'markdown'), ('html', 'html')], default='html', max_length=33),
        ),
    ]
