# Generated by Django 4.1.6 on 2023-02-16 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0002_alter_profile_user'),
        ('blog', '0007_season_podcast_season'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, max_length=225, null=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profile.profile')),
            ],
        ),
    ]
