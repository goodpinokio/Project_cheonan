# Generated by Django 4.2.3 on 2023-08-02 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_jobsuitability_job_job_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobsuitability',
            name='factor',
        ),
        migrations.RemoveField(
            model_name='jobsuitability',
            name='score',
        ),
        migrations.AddField(
            model_name='jobsuitability',
            name='score1_m',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobsuitability',
            name='score1_p',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobsuitability',
            name='score2_m',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobsuitability',
            name='score2_p',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobsuitability',
            name='score3_m',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobsuitability',
            name='score3_p',
            field=models.TextField(blank=True, null=True),
        ),
    ]
