# Generated by Django 3.1.4 on 2021-01-15 11:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cmspublications', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cmsmenus', '0001_initial'),
        ('cmscontexts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='navigationbaritem',
            name='inherited_content',
            field=models.ForeignKey(blank=True, help_text='Takes additional contents from a publication', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inherited_content', to='cmspublications.publication'),
        ),
        migrations.AddField(
            model_name='navigationbaritem',
            name='menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_menu', to='cmsmenus.navigationbar'),
        ),
        migrations.AddField(
            model_name='navigationbaritem',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='navigationbaritem_modified_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='navigationbaritem',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_parent', to='cmsmenus.navigationbaritem'),
        ),
        migrations.AddField(
            model_name='navigationbaritem',
            name='publication',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pub', to='cmspublications.publication'),
        ),
        migrations.AddField(
            model_name='navigationbaritem',
            name='webpath',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='linked_page', to='cmscontexts.webpath'),
        ),
        migrations.AddField(
            model_name='navigationbar',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='navigationbar_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='navigationbar',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='navigationbar_modified_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
