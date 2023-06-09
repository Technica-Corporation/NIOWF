import time
from django.db import models
from enum import Enum
from django.db import models
from django_enum_choices.fields import EnumChoiceField


class RelationshipType(Enum):
    owns = 'owns'
    requires = 'requires'
    instanceOf = 'instanceOf'
    cloneOf = 'cloneOf'


class MappingType(Enum):
    dashboard = 'dashboard'
    group = 'group'
    widget = 'widget_definition'


class DomainMappingsManager(models.Manager):

    # Group
    def get_group_dashboard_mappings(self, group_id):
        return self.filter(
            src_id=group_id,
            src_type=MappingType.group,
            relationship_type=RelationshipType.owns,
            dest_type=MappingType.dashboard
        )

    def get_group_dashboard_clone_mappings(self, group_dashboard_mappings):
        return self.filter(
            src_type=MappingType.dashboard,
            relationship_type=RelationshipType.cloneOf,
            dest_type=MappingType.dashboard,
            dest_id__in=list(group_dashboard_mappings.values_list("dest_id", flat=True))
        )

    def get_dashboard_clone_mappings(self, dashboard_id):
        return self.filter(
            src_type=MappingType.dashboard,
            relationship_type=RelationshipType.cloneOf,
            dest_type=MappingType.dashboard,
            dest_id=dashboard_id
        )

    def get_default_dashboard_ids(self, stack):
        return self.filter(
            src_id=stack.default_group_id,
            src_type=MappingType.group,
            relationship_type=RelationshipType.owns,
            dest_type=MappingType.dashboard
        ).values('dest_id')

    def get_user_cloned_dashboards_ids(self, default_dashboard_ids_query):
        return self.filter(
            src_type=MappingType.dashboard,
            relationship_type=RelationshipType.cloneOf,
            dest_id__in=default_dashboard_ids_query,
            dest_type=MappingType.dashboard
        ).values('src_id')

    def get_user_clone_of_groups_dashboard_domain_mapping(self, user_dashboard_id, default_dashboard_ids_query):
        return self.filter(
            src_type=MappingType.dashboard,
            src_id=user_dashboard_id,
            relationship_type=RelationshipType.cloneOf,
            dest_type=MappingType.dashboard,
            dest_id__in=default_dashboard_ids_query,
        )


class DomainMapping(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField(default=0)
    src_id = models.BigIntegerField()
    src_type = EnumChoiceField(MappingType, max_length=255)
    relationship_type = EnumChoiceField(
        RelationshipType,
        default=RelationshipType.owns,
        max_length=10,
        blank=True,
        null=True)
    dest_id = models.BigIntegerField()
    dest_type = EnumChoiceField(MappingType, max_length=255)

    objects = DomainMappingsManager()

    def __str__(self):
        return f'{self.src_type}:{self.src_id} {self.relationship_type} {self.dest_type}:{self.dest_id}'

    def save(self, *args, **kwargs):
        # Version saver for incrementing as time
        self.version = int(time.time())
        super(DomainMapping, self).save(*args, **kwargs)

    @classmethod
    def create_group_dashboard_mapping(cls, group, groupDashboard):
        mapping, _ = cls.objects.get_or_create(
            src_id=group.id,
            src_type=MappingType.group,
            relationship_type=RelationshipType.owns,
            dest_id=groupDashboard.id,
            dest_type=MappingType.dashboard
        )
        return mapping

    @classmethod
    def create_user_dashboard_mapping(cls, userDashboard, groupDashboard):
        mapping, _ = cls.objects.get_or_create(
            src_id=userDashboard.id,
            src_type=MappingType.dashboard,
            relationship_type=RelationshipType.cloneOf,
            dest_id=groupDashboard.id,
            dest_type=MappingType.dashboard
        )
        return mapping

    @classmethod
    def create_group_widget_mapping(cls, widget, group):
        return cls.objects.get_or_create(
            src_id=group.id,
            src_type=MappingType.group,
            relationship_type=RelationshipType.owns,
            dest_id=widget.id,
            dest_type=MappingType.widget
        )

    @classmethod
    def delete_group_widget_mapping(cls, widget, group):
        return cls.objects.filter(
            src_id=group.id,
            src_type=MappingType.group,
            relationship_type=RelationshipType.owns,
            dest_id=widget.id,
            dest_type=MappingType.widget
        ).delete()

    class Meta:
        managed = True
        db_table = 'domain_mapping'
