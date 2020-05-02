from django.db.models import Q
from attendees.occasions.models import Gathering


class GatheringService:

    @staticmethod
    def by_assembly_meets(assembly_slug, meet_slugs):
        return Gathering.objects.filter(
                    meet__slug__in=meet_slugs,
                    meet__assembly__slug=assembly_slug,
                ).order_by(
                    'meet',
                    '-start',
                )

    @staticmethod
    def by_family_meets(user, meet_slugs):
        """
        :query: Find all gatherings of all Attendances of the current user and their kid/care receiver, so all
                their "family" attending gatherings (including not joined characters) will show up.
        :param user: user object
        :param meet_slugs:
        :return:  all Gatherings of the logged in user and their kids/care receivers.
        """
        return Gathering.objects.filter(
            Q(meet__in=user.attendee.attendings.values_list('gathering__meet'))
            |
            Q(meet__in=user.attendee.related_ones.filter(
                from_attendee__scheduler=True
            ).values_list('attendings__gathering__meet')),
            meet__slug__in=meet_slugs,
            meet__assembly__division__organization__slug=user.organization.slug,
        ).order_by(
            'meet',
            '-start',
        )  # another way is to get assemblys from registration, but it relies on attendingmeet validations

    @staticmethod
    def by_organization_meets(organization_slug, meet_slugs):
        return Gathering.objects.filter(
            meet__slug__in=meet_slugs,
            meet__assembly__division__organization__slug=organization_slug,
        ).order_by(
            'meet',
            '-start',
        )
