from django.db.models import Q
from attendees.occasions.models import Attendance


class AttendanceService:

    @staticmethod
    def by_assembly_meets_characters_gathering_intervals(assembly_slug, meet_slugs, gathering_start, gathering_finish, character_slugs):
        return Attendance.objects.select_related(
                ).filter(
                    gathering__meet__assembly__slug=assembly_slug,
                    gathering__meet__slug__in=meet_slugs,
                    gathering__start__gte=gathering_start,
                    gathering__finish__lte=gathering_finish,
                    character__slug__in=character_slugs,
                ).order_by(
                    'gathering__meet',
                    '-gathering__start',
                    'character__display_order',
                )

    @staticmethod
    def by_organization_meets_gatherings_intervals(organization_slug, meet_slugs, gathering_ids, gathering_start, gathering_finish):
        """
        :query: Find all gatherings of all Attendances of the current user, query everyone's
                Attendances in the found gatherings, so all coworker's Attendances in the
                current user participated gatherings will also show up.
        :param organization_slug:
        :param meet_slugs:
        :param gathering_ids:
        :param gathering_start:
        :param gathering_finish:
        :return:  user participation Attendances with coworkers Attendances
        """
        return Attendance.objects.select_related(
                    'character',
                    'team',
                    'attending',
                    'gathering',
                    'attending__attendee',
                ).filter(
                    gathering__meet__assembly__division__organization__slug=organization_slug,
                    gathering__id__in=gathering_ids,
                    gathering__meet__slug__in=meet_slugs,
                    gathering__start__gte=gathering_start,
                    gathering__finish__lte=gathering_finish,
                ).order_by(
                    'gathering__meet',
                    '-gathering__start',
                    'character__display_order',
                )

    @staticmethod
    def by_family_meets_gathering_intervals(user, meet_slugs, gathering_start, gathering_finish):
        """
        :query: Find all gatherings of all Attendances of the current user and their kid/care receiver,
                , so all their "family" Attendances will show up.
        :param current_user:
        :param meet_slugs:
        :param gathering_start:
        :param gathering_finish:

        :return:  Attendances of the logged in user and their kids/care receivers
        """
        return Attendance.objects.select_related(
                    'character',
                    'team',
                    'attending',
                    'gathering',
                    'attending__attendee',
                ).filter(
                    Q(attending__attendee=user.attendee)
                    |
                    Q(attending__attendee__in=user.attendee.related_ones.filter(
                        from_attendee__scheduler=True,
                    )),
                    gathering__meet__assembly__division__organization__slug=user.organization.slug,
                    gathering__meet__slug__in=meet_slugs,
                    gathering__start__gte=gathering_start,
                    gathering__finish__lte=gathering_finish,
                ).order_by(
                    'gathering__meet',
                    '-gathering__start',
                    'character__display_order',
                )
