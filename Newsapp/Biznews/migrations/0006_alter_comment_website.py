# Generated by Django 4.2.3 on 2023-07-13 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biznews', '0005_comment_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='website',
            field=models.URLField(blank=True, default='example.com', max_length=100),
        ),
    ]
