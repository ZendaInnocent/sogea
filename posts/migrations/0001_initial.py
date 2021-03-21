# Generated by Django 3.1.7 on 2021-03-01 11:42

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import posts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_customuser_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.customuser')),
                ('profile_picture', models.ImageField(default='static/images/default_profile.png', upload_to=posts.models.featured_image_path)),
                ('website', models.URLField(blank=True)),
                ('country', django_countries.fields.CountryField(default='TZ', max_length=2, verbose_name='Country')),
                ('location', models.CharField(max_length=200)),
                ('display_email', models.BooleanField(default=False)),
                ('bio', models.TextField(blank=True)),
                ('youtube_link', models.URLField(verbose_name='Youtube URL')),
                ('facebook_link', models.URLField(verbose_name='Facebook URL')),
                ('instagram_link', models.URLField(verbose_name='Instagram URL')),
                ('linkedin_link', models.URLField(verbose_name='Linkedin URL')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(default='', editable=False, max_length=250)),
                ('overview', models.TextField()),
                ('content', ckeditor.fields.RichTextField()),
                ('comment_count', models.IntegerField(default=0)),
                ('view_count', models.PositiveIntegerField(default=0)),
                ('featured_image', models.ImageField(upload_to='featured_pictues')),
                ('featured', models.BooleanField(default=False)),
                ('language', models.CharField(choices=[('', 'select'), ('sw', 'Swahili'), ('en', 'English')], max_length=20)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved')], max_length=100)),
                ('membership', models.CharField(choices=[('', 'select'), ('Free', 'Free'), ('Premium', 'Premium')], max_length=100)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.author')),
                ('category', models.ForeignKey(default='uncategorized', on_delete=django.db.models.deletion.SET_DEFAULT, to='posts.category')),
            ],
        ),
    ]
