# Generated by Django 4.1.7 on 2023-03-27 19:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_enum_choices.choice_builders
import django_enum_choices.fields
import owf_groups.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OwfGroup',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('version', models.BigIntegerField(default=0)),
                ('status', django_enum_choices.fields.EnumChoiceField(choice_builder=django_enum_choices.choice_builders.value_value, choices=[('active', 'active'), ('inactive', 'inactive')], default=owf_groups.models.GroupStatus['active'], enum_class=owf_groups.models.GroupStatus, max_length=8)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('automatic', models.BooleanField(default=True)),
                ('display_name', models.CharField(blank=True, max_length=200, null=True)),
                ('stack_default', models.BooleanField(blank=True, default=False, null=True)),
            ],
            options={
                'db_table': 'owf_group',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='OwfGroupPeople',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owf_groups.owfgroup')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'owf_group_people',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='owfgroup',
            name='people',
            field=models.ManyToManyField(related_name='groups', through='owf_groups.OwfGroupPeople', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='owfgrouppeople',
            constraint=models.UniqueConstraint(fields=('group', 'person'), name='unique_owfgroup_people'),
        ),
    ]
