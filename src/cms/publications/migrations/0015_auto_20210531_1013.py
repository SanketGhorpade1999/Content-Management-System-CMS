# Generated by Django 3.2.3 on 2021-05-31 10:13

import cms.medias.validators
import cms.publications.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmspublications', '0014_auto_20210507_1618'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publicationgallery',
            options={'verbose_name_plural': 'Publication Media Collection'},
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, max_length=512, null=True, upload_to='images/categories', validators=[cms.medias.validators.validate_image_file_extension, cms.medias.validators.validate_file_size]),
        ),
        migrations.AlterField(
            model_name='publicationattachment',
            name='file',
            field=models.FileField(upload_to=cms.publications.models.publication_attachment_path, validators=[cms.medias.validators.validate_file_extension, cms.medias.validators.validate_file_size]),
        ),
    ]