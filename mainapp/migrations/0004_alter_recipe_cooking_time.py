# Generated by Django 5.0.6 on 2024-06-25 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_recipe_added_date_alter_recipe_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.PositiveIntegerField(default=0, verbose_name='Время приготовления (минут)'),
        ),
    ]
