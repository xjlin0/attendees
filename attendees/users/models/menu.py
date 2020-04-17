from django.contrib.auth.models import Group
from django.db import models
from django.contrib.postgres.fields.jsonb import JSONField
from mptt.models import MPTTModel, TreeForeignKey
from model_utils.models import TimeStampedModel, SoftDeletableModel
from attendees.whereabouts.models import Organization


class Menu(MPTTModel, TimeStampedModel, SoftDeletableModel):

    id = models.BigAutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID'
    )

    organization = models.ForeignKey(
        Organization,
        null=False,
        blank=False,
        default=0,
        on_delete=models.SET(0),
        help_text='Organization of the menu'
    )

    category = models.CharField(
        max_length=32,
        null=False,
        blank=False,
        default="main",
        help_text="Type of menu, such as 'main', 'side', etc"
    )

    parent = TreeForeignKey(
        'self',
        on_delete=models.SET(-1),
        null=True,
        blank=True,
        related_name='children'
    )

    html_type = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        help_text="HTML tags such as div or a",
    )

    urn = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="use relative path (including leading & ending slash '/') such as /0_organization_name/app/division/meets/",
    )

    display_name = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        help_text="description of the path, such as 'Character index page', 'divider between index and register links', etc",
    )

    display_order = models.SmallIntegerField(
        default=0,
        blank=False,
        null=False
    )

    infos = JSONField(
        null=True,
        blank=True,
        default=dict,
        help_text="HTML attributes & more such as {'class': 'dropdown-item'}. Please keep {} here even no data."
    )

    auth_groups = models.ManyToManyField(
        Group,
        through='MenuAuthGroup',
        related_name='auth_groups'
    )

    class MPTTMeta:
        order_insertion_by = ['display_order', 'display_name']

    class Meta:
        db_table = 'users_menus'
        constraints = [
            models.UniqueConstraint(fields=['organization', 'category', 'html_type', 'display_name'], name="organization_category_html_type_display_name")
        ]

# Todo: Raise ValueError if the instance.get_level() > 1 due to Boostrap 4 dropdown-submenu limit, or smartmenus will be needed.

    def __str__(self):
        return '%s %s %s URN: ...%s' % (self.organization_slug, self.category.upper(), self.display_name, self.urn[-40:] if self.urn else '')

    @property
    def organization_slug(self):
        return self.organization.slug if self.organization else ''
