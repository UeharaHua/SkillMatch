# Generated by Django 2.1.5 on 2019-03-30 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skillMatch', '0013_auto_20190328_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skillMatch.Student'),
        ),
    ]
