from django.db.models import Q
from attendees.occasions.models import Character


class CharacterService:

    @staticmethod
    def by_assembly_meets(assembly_slug, meet_slugs):
        return Character.objects.filter(
                    assembly__slug=assembly_slug,
                    assembly__meet__slug__in=meet_slugs,
                ).order_by(
                    'display_order',
                ).distinct()

    @staticmethod
    def by_family_meets_gathering_intervals(user):
        """
        :query: Find all gatherings of all Attendances of the current user and their kid/care receiver, so all
                their "family" attendances gathering's characters (including not joined characters) will show up.
        :param user: the logged in user
        :return:  all Characters of the logged in user and their kids/care receivers' gathering.

        """
        return Character.objects.filter(
                    Q(assembly__in=user.attendee.attendings.values_list('gathering__meet__assembly'))
                    |
                    Q(assembly__in=user.attendee.related_ones.filter(
                        from_attendee__scheduler=True
                    ).values_list('attendings__gathering__meet__assembly')),
                    assembly__division__organization__slug=user.organization.slug,
                ).order_by(
                    'display_order',
                )  # another way is to get assemblys from registration, but it relies on attendingmeet validations

    @staticmethod
    def by_organization_assemblys(organization_slug, assembly_slugs):
        return Character.objects.filter(
                    assembly__division__organization__slug=organization_slug,
                    assembly__slug__in=assembly_slugs,
                ).order_by(
                    'display_order',
                )
