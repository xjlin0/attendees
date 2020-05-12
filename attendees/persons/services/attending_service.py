from attendees.persons.models import Attending
from django.db.models.expressions import F
from django.db.models import Q


class AttendingService:

    @staticmethod
    def by_organization_meets_gatherings(meet_slugs, user_attended_gathering_ids, user_organization_slug):
        """
        :query: Find all gatherings of the current user, then list all attendings of the found gatherings.
                So if the current user didn't participate(attending), no info will be shown
        :param meet_slugs: slugs of the meets to be filtered
        :param user_attended_gathering_ids: primary gathering id of the Attendings to be filtered
        :param user_organization_slug: slugs of the user organization to be filtered
        :return: all Attendings with participating meets(group) and character(role)
        """
        return Attending.objects.select_related().prefetch_related().filter(
                    #registration_start/finish within the selected time period.
                    meets__slug__in=meet_slugs,
                    gathering__id__in=user_attended_gathering_ids,
                    meets__assembly__division__organization__slug=user_organization_slug,
                ).annotate(
                    meet=F('attendingmeet__meet__display_name'),
                    character=F('attendingmeet__character__display_name'),
                ).order_by(
                    'attendee',
                ).distinct()

    @staticmethod
    def by_family_organization_attendings(current_user, meet_slugs):
        """
        :query: Find all gatherings of the current user and their kids/care-receivers, then list all attendings of the
                found gatherings. So if the current user didn't participate(attending), no info will be shown.
        :param current_user: logged in user object, need to associate to an attendee
        :param meet_slugs: slugs of the meets to be filtered
        :return: all Attendings with participating meets(group) and character(role)
        """
        return Attending.objects.select_related().prefetch_related().filter(
                    Q(attendee=current_user.attendee)
                    |
                    Q(attendee__in=current_user.attendee.related_ones.filter(
                        from_attendee__scheduler=True,
                    )),
                    meets__slug__in=meet_slugs,
                    meets__assembly__division__organization__slug=current_user.organization.slug,
                ).annotate(
                    meet=F('attendingmeet__meet__display_name'),
                    character=F('attendingmeet__character__display_name'),
                ).order_by(
                    'attendee',
                )  # Todo: filter by start/finish within the selected time period.

    @staticmethod
    def by_assembly_meet_characters(assembly_slug, meet_slugs, character_slugs):
        """
        :param assembly_slug:
        :param meet_slugs:
        :param character_slugs:
        :return:
        """
        return Attending.objects.select_related().prefetch_related().filter(
                meets__slug__in=meet_slugs,
                attendingmeet__character__slug__in=character_slugs,
                meets__assembly__slug=assembly_slug,
            ).annotate(
                meet=F('attendingmeet__meet__display_name'),
                character=F('attendingmeet__character__display_name'),
            ).order_by(
                'attendee',
            )

