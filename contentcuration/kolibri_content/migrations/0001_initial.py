# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-02-14 22:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import jsonfield.fields
import kolibri.core.fields
import kolibri_content.models
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssessmentMetaData',
            fields=[
                ('id', kolibri_content.models.UUIDField(primary_key=True, serialize=False)),
                ('assessment_item_ids', jsonfield.fields.JSONField(default=[])),
                ('number_of_assessments', models.IntegerField()),
                ('mastery_model', jsonfield.fields.JSONField(default={})),
                ('randomize', models.BooleanField(default=False)),
                ('is_manipulable', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ChannelMetadata',
            fields=[
                ('id', kolibri_content.models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=400)),
                ('author', models.CharField(blank=True, max_length=400)),
                ('version', models.IntegerField(default=0)),
                ('thumbnail', models.TextField(blank=True)),
                ('last_updated', kolibri.core.fields.DateTimeTzField(null=True)),
                ('min_schema_version', models.CharField(max_length=50)),
                ('root_pk', kolibri_content.models.UUIDField()),
            ],
        ),
        migrations.CreateModel(
            name='ContentNode',
            fields=[
                ('id', kolibri_content.models.UUIDField(primary_key=True, serialize=False)),
                ('license_name', models.CharField(blank=True, max_length=50, null=True)),
                ('license_description', models.CharField(blank=True, max_length=400, null=True)),
                ('title', models.CharField(max_length=200)),
                ('content_id', kolibri_content.models.UUIDField(db_index=True)),
                ('channel_id', kolibri_content.models.UUIDField(db_index=True)),
                ('description', models.CharField(blank=True, max_length=400, null=True)),
                ('sort_order', models.FloatField(blank=True, null=True)),
                ('license_owner', models.CharField(blank=True, max_length=200)),
                ('author', models.CharField(blank=True, max_length=200)),
                ('kind', models.CharField(blank=True, choices=[(b'topic', b'Topic'), (b'video', b'Video'), (b'audio', b'Audio'), (b'exercise', b'Exercise'), (b'document', b'Document'), (b'html5', b'HTML5 App')], max_length=200)),
                ('available', models.BooleanField(default=False)),
                ('stemmed_metaphone', models.CharField(blank=True, max_length=1800)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('has_prerequisite', models.ManyToManyField(blank=True, related_name='prerequisite_for', to='content.ContentNode')),
            ],
            options={
                'ordering': ('lft',),
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ContentTag',
            fields=[
                ('id', kolibri_content.models.UUIDField(primary_key=True, serialize=False)),
                ('tag_name', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', kolibri_content.models.UUIDField(primary_key=True, serialize=False)),
                ('available', models.BooleanField(default=False)),
                ('preset', models.CharField(blank=True, choices=[(b'high_res_video', b'High Resolution'), (b'low_res_video', b'Low Resolution'), (b'vector_video', b'Vectorized'), (b'video_thumbnail', b'Thumbnail'), (b'video_subtitle', b'Subtitle'), (b'audio', b'Audio'), (b'audio_thumbnail', b'Thumbnail'), (b'document', b'Document'), (b'document_thumbnail', b'Thumbnail'), (b'exercise', b'Exercise'), (b'exercise_thumbnail', b'Thumbnail'), (b'exercise_image', b'Exercise Image'), (b'exercise_graphie', b'Exercise Graphie'), (b'channel_thumbnail', b'Channel Thumbnail'), (b'topic_thumbnail', b'Thumbnail'), (b'html5_zip', b'HTML5 Zip'), (b'html5_thumbnail', b'HTML5 Thumbnail')], max_length=150)),
                ('supplementary', models.BooleanField(default=False)),
                ('thumbnail', models.BooleanField(default=False)),
                ('priority', models.IntegerField(blank=True, db_index=True, null=True)),
                ('extension', models.CharField(blank=True, choices=[(b'mp4', b'MP4 Video'), (b'vtt', b'VTT Subtitle'), (b'srt', b'SRT Subtitle'), (b'mp3', b'MP3 Audio'), (b'pdf', b'PDF Document'), (b'jpg', b'JPG Image'), (b'jpeg', b'JPEG Image'), (b'png', b'PNG Image'), (b'gif', b'GIF Image'), (b'json', b'JSON'), (b'svg', b'SVG Image'), (b'perseus', b'Perseus Exercise'), (b'zip', b'HTML5 Zip')], max_length=40)),
                ('file_size', models.IntegerField(blank=True, null=True)),
                ('checksum', models.CharField(blank=True, max_length=400)),
                ('contentnode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='content.ContentNode')),
            ],
            options={
                'ordering': ['priority'],
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('lang_code', models.CharField(db_index=True, max_length=3)),
                ('lang_subcode', models.CharField(blank=True, db_index=True, max_length=10, null=True)),
                ('lang_name', models.CharField(blank=True, max_length=100, null=True)),
                ('lang_direction', models.CharField(choices=[(b'ltr', b'Left to Right'), (b'rtl', b'Right to Left')], default=b'ltr', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_name', models.CharField(max_length=50)),
                ('license_description', models.CharField(blank=True, max_length=400, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LocalFile',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('extension', models.CharField(blank=True, choices=[(b'mp4', b'MP4 Video'), (b'vtt', b'VTT Subtitle'), (b'srt', b'SRT Subtitle'), (b'mp3', b'MP3 Audio'), (b'pdf', b'PDF Document'), (b'jpg', b'JPG Image'), (b'jpeg', b'JPEG Image'), (b'png', b'PNG Image'), (b'gif', b'GIF Image'), (b'json', b'JSON'), (b'svg', b'SVG Image'), (b'perseus', b'Perseus Exercise'), (b'zip', b'HTML5 Zip')], max_length=40)),
                ('available', models.BooleanField(default=False)),
                ('file_size', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='file',
            name='lang',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='content.Language'),
        ),
        migrations.AddField(
            model_name='file',
            name='local_file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='content.LocalFile'),
        ),
        migrations.AddField(
            model_name='contentnode',
            name='lang',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='content.Language'),
        ),
        migrations.AddField(
            model_name='contentnode',
            name='license',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='content.License'),
        ),
        migrations.AddField(
            model_name='contentnode',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='content.ContentNode'),
        ),
        migrations.AddField(
            model_name='contentnode',
            name='related',
            field=models.ManyToManyField(blank=True, related_name='_contentnode_related_+', to='content.ContentNode'),
        ),
        migrations.AddField(
            model_name='contentnode',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tagged_content', to='content.ContentTag'),
        ),
        migrations.AddField(
            model_name='channelmetadata',
            name='root',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.ContentNode'),
        ),
        migrations.AddField(
            model_name='assessmentmetadata',
            name='contentnode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assessmentmetadata', to='content.ContentNode'),
        ),
        migrations.AlterIndexTogether(
            name='contentnode',
            index_together=set([('level', 'channel_id', 'kind'), ('level', 'channel_id', 'available')]),
        ),
    ]
