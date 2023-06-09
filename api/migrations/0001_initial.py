# Generated by Django 4.2.1 on 2023-06-01 19:44

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=256)),
                ('portfolio', models.TextField()),
                ('experience', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('education', models.CharField(max_length=256)),
                ('salary', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('specialty', models.CharField(max_length=256)),
                ('grade', models.CharField(max_length=25)),
                ('status', models.CharField(max_length=25)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='every_resume', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
