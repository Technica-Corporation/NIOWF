# Generated by Django 4.1.7 on 2023-03-27 19:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('intents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WidgetDefinition',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('version', models.BigIntegerField(default=0)),
                ('visible', models.BooleanField()),
                ('image_url_medium', models.CharField(max_length=2083)),
                ('image_url_small', models.CharField(max_length=2083)),
                ('singleton', models.BooleanField(default=False)),
                ('width', models.IntegerField()),
                ('widget_version', models.CharField(blank=True, max_length=2083, null=True)),
                ('height', models.IntegerField()),
                ('widget_url', models.CharField(max_length=2083)),
                ('widget_guid', models.CharField(default=uuid.uuid4, max_length=255, unique=True)),
                ('display_name', models.CharField(blank=True, max_length=256)),
                ('background', models.BooleanField(blank=True, null=True)),
                ('universal_name', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('descriptor_url', models.CharField(blank=True, max_length=2083, null=True)),
                ('description', models.CharField(blank=True, max_length=4000, null=True)),
                ('mobile_ready', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'widget_definition',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='WidgetDefIntent',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('version', models.BigIntegerField(default=0)),
                ('receive', models.BooleanField()),
                ('send', models.BooleanField()),
                ('intent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intents.intent')),
                ('widget_definition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='widgets.widgetdefinition')),
            ],
            options={
                'db_table': 'widget_def_intent',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='WidgetType',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('version', models.BigIntegerField()),
                ('name', models.CharField(max_length=255)),
                ('display_name', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'widget_type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='WidgetDefIntentDataTypes',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('intent_data_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intents.intentdatatype')),
                ('widget_definition_intent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='widgets.widgetdefintent')),
            ],
            options={
                'db_table': 'widget_def_intent_data_types',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='WidgetDefinitionWidgetTypes',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('widget_definition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='widgets.widgetdefinition')),
                ('widget_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='widgets.widgettype')),
            ],
            options={
                'db_table': 'widget_definition_widget_types',
                'managed': True,
                'unique_together': {('widget_definition', 'widget_type')},
            },
        ),
        migrations.AddField(
            model_name='widgetdefinition',
            name='types',
            field=models.ManyToManyField(related_name='widgets', through='widgets.WidgetDefinitionWidgetTypes', to='widgets.widgettype'),
        ),
    ]
