from pytz import timezone
from datetime import datetime
from django.conf import settings
from urllib import parse


def common_variables(request):  # TODO move organization info to view
    tzname = request.COOKIES.get('timezone') or settings.CLIENT_DEFAULT_TIME_ZONE
    user_organization_name = settings.PROJECT_NAME
    user_organization_name_slug = '0_organization_slug'

    if request.user.is_authenticated:
        user_organization = request.user.organization
        user_organization_name = user_organization.display_name
        user_organization_name_slug = user_organization.slug
    return {
        'timezone_name': datetime.now(timezone(parse.unquote(tzname))).tzname(),
        'user_organization_name': user_organization_name,
        'user_organization_name_slug': user_organization_name_slug,
    }  # Todo pass in user_division_slugs based on users' auth_group to display menu
