# Generated by Django 4.1.4 on 2023-04-14 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('command', '0005_remove_command_command_remove_command_keyword_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='command',
            name='css',
            field=models.TextField(blank=True, max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='command',
            name='html',
            field=models.TextField(blank=True, max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='command',
            name='js',
            field=models.TextField(blank=True, max_length=3000, null=True),
        ),
    ]