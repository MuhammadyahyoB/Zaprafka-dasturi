# Generated by Django 5.0.6 on 2024-05-15 21:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Yoqilgituri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='zaprafka',
            name='lan',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zaprafka',
            name='lat',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.RemoveField(
            model_name='zaprafka',
            name='category',
        ),
        migrations.AddField(
            model_name='zaprafka',
            name='yoqilgituri',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.yoqilgituri'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Zaprafkacategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
                ('zaprafka', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.zaprafka')),
            ],
        ),
        migrations.AddField(
            model_name='zaprafka',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.category'),
            preserve_default=False,
        ),
    ]
