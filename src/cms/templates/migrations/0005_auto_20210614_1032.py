# Generated by Django 3.2.3 on 2021-06-14 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmstemplates', '0004_alter_pagetemplate_template_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagetemplate',
            name='name',
            field=models.CharField(blank=True, default='', max_length=160),
        ),
        migrations.AlterField(
            model_name='pagetemplate',
            name='note',
            field=models.TextField(blank=True, default='', help_text='Editorial Board Notes, not visible by public.'),
        ),
        migrations.AlterField(
            model_name='templateblock',
            name='content',
            field=models.TextField(blank=True, default='', help_text='according to the block template schema'),
        ),
        migrations.AlterField(
            model_name='templateblock',
            name='description',
            field=models.TextField(blank=True, default='', help_text='Description of this block'),
        ),
        migrations.AlterField(
            model_name='templateblock',
            name='name',
            field=models.CharField(blank=True, default='', help_text='Specify the container section in the template where this block would be rendered.', max_length=60),
        ),
    ]
