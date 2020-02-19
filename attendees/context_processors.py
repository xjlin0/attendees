from pytz import timezone
from datetime import datetime
from django.conf import settings
from urllib import parse


def common_variables(request):
    tzname = request.COOKIES.get('timezone') or settings.CLIENT_DEFAULT_TIME_ZONE
    return {
        'timezone_name': datetime.now(timezone(parse.unquote(tzname))).tzname(),
        'user_organization_name': request.user.organization.display_name if request.user.organization else '',
        'user_organization_name_slug': request.user.organization.slug if request.user.organization else '0_organization_slug',
    }
