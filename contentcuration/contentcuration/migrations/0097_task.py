# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-28 20:19
from __future__ import unicode_literals

import contentcuration.models
from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ('contentcuration', '0096_merge_20181222_0008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_type', models.CharField(max_length=50)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(max_length=10)),
                ('is_progress_tracking', models.BooleanField(default=False)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task', to=settings.AUTH_USER_MODEL)),
                ('task_id', contentcuration.models.UUIDField(db_index=True, default=uuid.uuid4, max_length=32)),
            ],
        ),
        migrations.AlterField(
            model_name='formatpreset',
            name='id',
            field=models.CharField(choices=[(b'high_res_video', b'High Resolution'), (b'low_res_video', b'Low Resolution'), (b'video_thumbnail', b'Thumbnail'), (b'video_subtitle', b'Subtitle'), (b'video_dependency', b'Video (dependency)'), (b'audio', b'Audio'), (b'audio_thumbnail', b'Thumbnail'), (b'document', b'Document'), (b'epub', b'ePub Document'), (b'document_thumbnail', b'Thumbnail'), (b'exercise', b'Exercise'), (b'exercise_thumbnail', b'Thumbnail'), (b'exercise_image', b'Exercise Image'), (b'exercise_graphie', b'Exercise Graphie'), (b'channel_thumbnail', b'Channel Thumbnail'), (b'topic_thumbnail', b'Thumbnail'), (b'html5_zip', b'HTML5 Zip'), (b'html5_dependency', b'HTML5 Dependency (Zip format)'), (b'html5_thumbnail', b'HTML5 Thumbnail')], max_length=150, primary_key=True, serialize=False),
        ),
    ]
