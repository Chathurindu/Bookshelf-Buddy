# Generated by Django 4.2.4 on 2023-08-09 02:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('publication_date', models.DateField(blank=True, null=True)),
                ('isbn', models.CharField(blank=True, max_length=13, null=True, unique=True)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='covers/')),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
