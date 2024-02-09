# Generated by Django 3.1.4 on 2021-01-18 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmspublications', '0004_auto_20210118_0904'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicationContextRelated',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('order', models.IntegerField(blank=True, default=10, null=True)),
                ('is_active', models.BooleanField()),
                ('publication_context', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_page', to='cmspublications.publicationcontext')),
                ('related', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_publication_context', to='cmspublications.publicationcontext')),
            ],
            options={
                'verbose_name_plural': 'Related Publication Contexts',
                'unique_together': {('publication_context', 'related')},
            },
        ),
        migrations.DeleteModel(
            name='PublicationRelated',
        ),
    ]