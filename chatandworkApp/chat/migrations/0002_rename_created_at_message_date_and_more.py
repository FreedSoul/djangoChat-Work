# Generated by Django 5.0.6 on 2024-06-21 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='created_at',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='updated_at',
            new_name='updated',
        ),
        migrations.AddField(
            model_name='message',
            name='room',
            field=models.CharField(default='Default', max_length=1000),
        ),
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.TextField(max_length=10000),
        ),
    ]
