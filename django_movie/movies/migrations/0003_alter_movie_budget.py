# Generated by Django 3.2.4 on 2021-06-15 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_rating_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='budget',
            field=models.PositiveIntegerField(default=0, help_text='указывать сумму в долларах', verbose_name='Бюджет'),
        ),
    ]
