# Generated by Django 3.2 on 2023-06-11 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserCenter', '0005_auto_20230611_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='hash_code',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddIndex(
            model_name='job',
            index=models.Index(fields=['hash_code'], name='job_hash_co_2b97bd_idx'),
        ),
    ]
