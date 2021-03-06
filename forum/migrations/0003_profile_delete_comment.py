# Generated by Django 4.0.3 on 2022-05-05 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0002_comment_alter_forum_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True)),
                ('facebook', models.CharField(blank=True, max_length=50, null=True)),
                ('twitter', models.CharField(blank=True, max_length=50, null=True)),
                ('instagram', models.CharField(blank=True, max_length=50, null=True)),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.forum')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
