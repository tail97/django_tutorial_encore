# Generated by Django 4.1.3 on 2022-12-02 02:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0002_rename_content_article_contents_alter_article_cdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='mdate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='article',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
