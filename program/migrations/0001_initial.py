# Generated by Django 2.2.10 on 2020-02-28 06:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('name_ko', models.CharField(db_index=True, max_length=100, null=True)),
                ('name_en', models.CharField(db_index=True, max_length=100, null=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('visible', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProgramDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('name_ko', models.CharField(max_length=100, null=True)),
                ('name_en', models.CharField(max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('desc_ko', models.TextField(blank=True, null=True)),
                ('desc_en', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('name_ko', models.CharField(db_index=True, max_length=100, null=True)),
                ('name_en', models.CharField(db_index=True, max_length=100, null=True)),
                ('organization', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, db_index=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='speaker')),
                ('desc', models.TextField(blank=True, null=True)),
                ('desc_ko', models.TextField(blank=True, null=True)),
                ('desc_en', models.TextField(blank=True, null=True)),
                ('info', jsonfield.fields.JSONField(blank=True, default=dict, help_text='help-text-for-speaker-info')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='TutorialProposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('brief', models.TextField(max_length=1000)),
                ('desc', models.TextField()),
                ('comment', models.TextField(blank=True, max_length=4000, null=True)),
                ('difficulty', models.CharField(choices=[('B', 'Beginner'), ('I', 'Intermediate'), ('E', 'Experienced')], max_length=1)),
                ('duration', models.CharField(choices=[('S', '1 hour'), ('M', '2 hours'), ('L', '4 hours')], max_length=1)),
                ('language', models.CharField(choices=[('E', 'English'), ('K', 'Korean')], default='E', max_length=1)),
                ('capacity', models.IntegerField()),
                ('confirmed', models.BooleanField(default=False)),
                ('begin_date', models.DateField(blank=True, null=True)),
                ('begin_time', models.TimeField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('option', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.Option', verbose_name='구매 티켓 종류')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SprintProposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('language', models.CharField(max_length=255)),
                ('project_url', models.CharField(max_length=1024)),
                ('project_brief', models.TextField(max_length=1000)),
                ('contribution_desc', models.TextField()),
                ('comment', models.TextField(blank=True, max_length=4000, null=True)),
                ('confirmed', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('brief', models.TextField(max_length=1000)),
                ('desc', models.TextField(max_length=4000)),
                ('comment', models.TextField(blank=True, max_length=4000, null=True)),
                ('difficulty', models.CharField(choices=[('B', 'Beginner'), ('I', 'Intermediate'), ('E', 'Experienced')], max_length=1)),
                ('duration', models.CharField(choices=[('S', '25 mins'), ('L', '40 mins')], max_length=1)),
                ('language', models.CharField(choices=[('E', 'English'), ('K', 'Korean')], default='E', max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProgramTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('name_ko', models.CharField(max_length=100, null=True)),
                ('name_en', models.CharField(max_length=100, null=True)),
                ('begin', models.TimeField()),
                ('end', models.TimeField()),
                ('day', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='program.ProgramDate')),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('name_ko', models.CharField(db_index=True, max_length=255, null=True)),
                ('name_en', models.CharField(db_index=True, max_length=255, null=True)),
                ('brief', models.TextField(blank=True, null=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('desc_ko', models.TextField(blank=True, null=True)),
                ('desc_en', models.TextField(blank=True, null=True)),
                ('slide_url', models.CharField(blank=True, max_length=255, null=True)),
                ('pdf_url', models.CharField(blank=True, max_length=255, null=True)),
                ('video_url', models.CharField(blank=True, max_length=255, null=True)),
                ('difficulty', models.CharField(choices=[('B', 'Beginner'), ('I', 'Intermediate'), ('E', 'Experienced')], default='B', max_length=1)),
                ('duration', models.CharField(choices=[('S', '25 mins'), ('L', '40 mins')], default='S', max_length=1)),
                ('language', models.CharField(choices=[('E', 'English'), ('K', 'Korean')], default='E', max_length=1)),
                ('is_recordable', models.BooleanField(default=True)),
                ('is_breaktime', models.BooleanField(default=False)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='program.ProgramCategory')),
                ('date', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='program.ProgramDate')),
                ('rooms', models.ManyToManyField(blank=True, to='program.Room')),
                ('speakers', models.ManyToManyField(blank=True, to='program.Speaker')),
                ('times', models.ManyToManyField(blank=True, to='program.ProgramTime')),
            ],
        ),
        migrations.CreateModel(
            name='TutorialCheckin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutorial', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='program.TutorialProposal')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'tutorial')},
            },
        ),
        migrations.CreateModel(
            name='SprintCheckin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sprint', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='program.SprintProposal')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'sprint')},
            },
        ),
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='program.Program')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'program')},
            },
        ),
    ]