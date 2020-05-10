from pytz import timezone
from datetime import datetime
from django.conf import settings
from urllib import parse

from attendees.users.models import Menu


def common_variables(request):  # TODO move organization info to view
    tzname = request.COOKIES.get('timezone') or settings.CLIENT_DEFAULT_TIME_ZONE
    user_organization_name = settings.PROJECT_NAME
    user_organization_name_slug = '0_organization_slug'
    main_menus = Menu.objects.filter(
        auth_groups__in=request.user.groups.all(),
        category='main',
        menuauthgroup__read=True,
    ).distinct()
    if request.user.is_authenticated and request.user.organization:
        user_organization = request.user.organization
        user_organization_name = user_organization.display_name
        user_organization_name_slug = user_organization.slug
    return {
        'timezone_name': datetime.now(timezone(parse.unquote(tzname))).tzname(),
        'user_organization_name': user_organization_name,
        'user_organization_name_slug': user_organization_name_slug,
        'main_menus': main_menus,
    }
