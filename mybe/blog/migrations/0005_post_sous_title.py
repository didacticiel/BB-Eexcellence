# Generated by Django 5.1.4 on 2025-01-06 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='sous_title',
            field=models.CharField(blank=True, db_index=True, max_length=200, null=True),
        ),
    ]
