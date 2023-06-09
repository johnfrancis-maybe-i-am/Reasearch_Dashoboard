# Generated by Django 4.2 on 2023-04-07 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_comments_rename_post_academicdetails_workprocess'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicdetails',
            name='file',
            field=models.FileField(upload_to='academicdocs/'),
        ),
        migrations.AlterField(
            model_name='workprocess',
            name='comments',
            field=models.ManyToManyField(blank=True, to='student.comments'),
        ),
        migrations.AlterField(
            model_name='workprocess',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
