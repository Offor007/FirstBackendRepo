# Generated by Django 4.2.3 on 2023-07-13 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biznews', '0006_alter_comment_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='website',
            field=models.URLField(blank=True, default='None', max_length=100),
        ),
    ]