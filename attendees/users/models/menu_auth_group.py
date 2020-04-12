from django.db import models
from django.contrib.auth.models import Group
from model_utils.models import TimeStampedModel, SoftDeletableModel
from attendees.users.models import Menu


class MenuAuthGroup(TimeStampedModel, SoftDeletableModel):

    id = models.BigAutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID'
    )

    auth_group = models.ForeignKey(
        Group,
        null=False,
        blank=False,
        default=0,
        on_delete=models.SET(0),
    )

    read = models.BooleanField(
        null=False,
        blank=False,
        default=True,
    )

    write = models.BooleanField(
        null=False,
        blank=False,
        default=True,
    )

    menu = models.ForeignKey(
        Menu,
        null=False,
        blank=False,
        default=0,
        on_delete=models.SET(0),
    )

    class Meta:
        db_table = 'users_menu_auth_groups'
        constraints = [
            models.UniqueConstraint(fields=['auth_group', 'menu'], name="auth_group_menu")
        ]
