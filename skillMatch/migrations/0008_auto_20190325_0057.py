# Generated by Django 2.1.5 on 2019-03-25 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skillMatch', '0007_student_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='picture',
            field=models.ImageField(default='media/default-user.jpg', upload_to='images/'),
        ),
    ]
