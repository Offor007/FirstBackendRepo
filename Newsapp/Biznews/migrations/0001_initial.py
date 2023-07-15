# Generated by Django 4.2.3 on 2023-07-08 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='News_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='thumbnail')),
                ('article', models.TextField()),
                ('publication_date', models.DateField(auto_now_add=True)),
                ('title', models.CharField(max_length=200)),
                ('details', models.TextField()),
                ('sub_title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=50)),
                ('views', models.PositiveIntegerField(default=0)),
                ('comment', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Biznews.category')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('comment', models.TextField()),
                ('comment_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('news_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Biznews.news_details')),
            ],
        ),
    ]