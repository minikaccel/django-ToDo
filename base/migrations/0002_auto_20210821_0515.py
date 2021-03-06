# Generated by Django 3.2.6 on 2021-08-21 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={},
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, help_text='Not required', null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(blank=True, help_text='Not required', max_length=255, null=True),
        ),
        migrations.AlterOrderWithRespectTo(
            name='task',
            order_with_respect_to='user',
        ),
    ]
