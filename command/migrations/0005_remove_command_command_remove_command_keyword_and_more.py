# Generated by Django 4.1.4 on 2023-04-14 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('command', '0004_article_date_command_date_command_difficulty_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='command',
            name='command',
        ),
        migrations.RemoveField(
            model_name='command',
            name='keyword',
        ),
        migrations.AddField(
            model_name='command',
            name='css',
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
        migrations.AddField(
            model_name='command',
            name='html',
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
        migrations.AddField(
            model_name='command',
            name='js',
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
    ]
