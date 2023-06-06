# Generated by Django 3.2 on 2023-06-06 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserCenter', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='worker',
            options={'ordering': ['uid']},
        ),
        migrations.RemoveIndex(
            model_name='worker',
            name='worker_wid_20c430_idx',
        ),
        migrations.RenameField(
            model_name='worker',
            old_name='wid',
            new_name='uid',
        ),
        migrations.AddIndex(
            model_name='worker',
            index=models.Index(fields=['uid'], name='worker_uid_c64213_idx'),
        ),
    ]