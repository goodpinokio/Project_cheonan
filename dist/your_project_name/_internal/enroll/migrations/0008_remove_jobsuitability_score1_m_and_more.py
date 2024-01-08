# Generated by Django 4.2.3 on 2023-12-28 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0007_characteristic_remove_jobsuitability_score1_m_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobsuitability',
            name='score1_m',
        ),
        migrations.RemoveField(
            model_name='jobsuitability',
            name='score1_p',
        ),
        migrations.RemoveField(
            model_name='jobsuitability',
            name='score2_m',
        ),
        migrations.RemoveField(
            model_name='jobsuitability',
            name='score2_p',
        ),
        migrations.RemoveField(
            model_name='jobsuitability',
            name='score3_m',
        ),
        migrations.RemoveField(
            model_name='jobsuitability',
            name='score3_p',
        ),
        migrations.DeleteModel(
            name='Characteristic',
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
