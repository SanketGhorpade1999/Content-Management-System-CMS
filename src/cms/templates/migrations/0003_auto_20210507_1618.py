# Generated by Django 3.1.6 on 2021-05-07 16:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cmstemplates', '0002_auto_20210119_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagetemplate',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pagetemplate_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pagetemplate',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pagetemplate_modified_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pagetemplateblock',
            name='block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cmstemplates.templateblock'),
        ),
        migrations.AlterField(
            model_name='pagetemplateblock',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pagetemplateblock_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pagetemplateblock',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pagetemplateblock_modified_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='templateblock',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='templateblock_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='templateblock',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='templateblock_modified_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
