# Generated by Django 2.1.7 on 2019-04-03 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utility', '0002_auto_20190326_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('artwork', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='utility.File')),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('artwork', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='utility.File')),
            ],
        ),
        migrations.AddField(
            model_name='podcast',
            name='chapter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='podcasts', to='podcast.Season'),
        ),
        migrations.AddField(
            model_name='podcast',
            name='file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='podcasts', to='utility.File', verbose_name='Course file'),
        ),
    ]
