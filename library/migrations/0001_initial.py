# Generated by Django 3.2.3 on 2021-05-27 07:02

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
            name='StudentMainTable',
            fields=[
                ('stdid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('email_id', models.TextField(blank=True, null=True)),
                ('degree', models.TextField()),
                ('branch', models.TextField()),
                ('persuing_year', models.TextField()),
                ('doj', models.TextField()),
            ],
            options={
                'db_table': 'student',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookMainCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('roll_num', models.CharField(max_length=200, null=True)),
                ('studying', models.CharField(max_length=200, null=True)),
                ('branch', models.CharField(max_length=200, null=True)),
                ('pyr', models.IntegerField(null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookSubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category_name', models.CharField(max_length=100)),
                ('main_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library.bookmaincategory')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn_num', models.CharField(help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=20, verbose_name='ISBN')),
                ('title', models.CharField(max_length=30, null=True)),
                ('summary', models.CharField(max_length=200, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.author')),
                ('main_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library.bookmaincategory')),
                ('sub_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library.booksubcategory')),
            ],
        ),
    ]
