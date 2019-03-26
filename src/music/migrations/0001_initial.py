# Generated by Django 2.1.7 on 2019-03-03 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utility', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, null=True)),
                ('artwork', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='utility.File')),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='musics', to='music.Album')),
                ('artwork', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='music_artwork', to='utility.File')),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='musics', to='utility.File', verbose_name='Music file')),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('artwork', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='utility.File')),
            ],
        ),
        migrations.AddField(
            model_name='music',
            name='playlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='musics', to='music.Playlist'),
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='music.Artist'),
        ),
        migrations.AddField(
            model_name='album',
            name='artwork',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='utility.File'),
        ),
    ]
