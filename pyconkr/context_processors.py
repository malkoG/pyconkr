from collections import OrderedDict

from django.utils import timezone
from django.conf import settings
from django.contrib.flatpages.models import FlatPage
from django.db.models import Count
from django.utils.translation import ugettext_lazy as _

from pyconkr.models import Banner
from sponsor.models import SponsorLevel
from program.models import Speaker


def default(request):
    title = None
    # remove i18n_patterns prefix for flatpage
    url = request.path.replace('/' + request.LANGUAGE_CODE, '')
    if settings.FORCE_SCRIPT_NAME:
        url = url[len(settings.FORCE_SCRIPT_NAME):]
    base_content = FlatPage.objects.filter(url=url).first()

    submenu = None
    menu = OrderedDict([
        (
            'about', {
                'title': _('About'),
                'submenu': OrderedDict([
                    ('pyconkr', {'title': _('About PyCon Korea 2020')}),
                    ('venue', {'title': _('Venue'), 'disable': True}),
                    ('schedule', {'title': _('Important Dates')}),
                    ('patron', {'title': _('Patrons')}),
                    ('coc', {'title': _('Code of Conduct')}),
                    ('orginizing-team', {'title': _('Organizing Team')}),
                    ('previous-pyconkr', {'title': _('Previous PyCon Korea')}),
                ])
            }
        ),
        (
            'support', {
                'title': _('Support'),
                'submenu': OrderedDict([
                    ('financial-aid', {'title': _('Financial Aid'), 'disable': True}),
                    ('visa-sponsing', {'title': _('Visa Sponsing'), 'disable': True}),
                    ('child-care', {'title': _('Child Care'), 'disable': True}),
                    ('speech2text', {
                     'title': _('Speech to Text Translation')}),
                ])
            },
        ),
        (
            'program', {
                'title': _('Program'),
                'submenu': OrderedDict([
                    ('keynote', {'title': _('Keynotes'), 'disable': True}),
                    ('talks', {'title': _('Talks')}),
                    ('lightning-talk', {'title': _('Lightning Talk'), 'disable': True}),
                    ('openspace', {'title': _('Open Spaces'), 'disable': True}),
                    ('tutorial', {'title': _('Tutorial'), 'disable': True}),
                    ('sprint', {'title': _('Sprint'), 'disable': True}),
                    ('youngcoder', {'title': _('Young Coder'), 'disable': True}),
                ])
            }
        ),
        (
            'timetable', {
                'title': _('Timetable'),
                'disable': True,
                'submenu': OrderedDict([
                    ('conference', {'title': _('Conference')}),
                    ('tutorial', {'title': _('Tutorial')}),
                    ('sprint', {'title': _('Sprint')}),
                ])
            }
        ),
        (
            'contribution', {
                'title': _('Contribution'),
                'submenu': OrderedDict([
                    ('about', {'title': _('About Contribution')}),
                    ('cfp/guide', {'title': _('How to Submit a Proposal')}),
                    ('cfp', {'title': _('Proposing a Talk')}),
                    ('review-talk-proposal',
                     {'title': _('Review Talk Proposal')}),
                    ('proposing-tutorial',
                     {'title': _('Proposing a Tutorial'), 'disable': True}),
                    ('recommending-keynote',
                     {'title': _('Recommending Keynote')}),
                    ('volunteer', {'title': _('Volunteer'), 'disable': True}),
                    ('video-subtitle', {'title': _('Video Subtitle')}),
                ])
            }
        ),
        (
            'sponsor', {
                'title': _('Sponsor'),
                'submenu': OrderedDict([
                    ('prospectus', {'title': _('Prospectus')}),
                    ('benefit', {'title': _('Benefit'), 'disable': True}),
                    ('join', {'title': _('Join as Sponsor')}),
                    ('faq', {'title': _('FAQ')}),
                    ('terms-of-sponsor', {'title': _('Terms of Sponsor')}),
                    ('virtual_booth', {'title': _('Virtual Booth')}),
                ])
            }
        )
    ])

    for k, v in menu.items():
        path = '/{}/'.format(k)

        if url.startswith(path):
            v['active'] = True
            title = v['title']

            if 'submenu' in v:
                submenu = v['submenu']

                for sk, sv in v['submenu'].items():
                    sv['path'] = '{}{}/'.format(path, sk)
                    subpath = sv['path']

                    if url == subpath:
                        sv['active'] = True
                        title = sv['title']

    now = timezone.now()
    banners = Banner.objects.filter(begin__lte=now, end__gte=now)

    c = {
        'menu': menu,
        'submenu': submenu,
        'banners': banners,
        'title': title,
        'domain': settings.DOMAIN,
        'base_content': base_content.content if base_content else '',
    }
    return c


def profile(request):
    speaker = None
    programs = None

    if request.user.is_authenticated:
        speaker = Speaker.objects.filter(email=request.user.email).first()
        if speaker:
            programs = speaker.program_set.all()

    return {
        'my_speaker': speaker,
        'my_programs': programs,
    }


def sponsors(request):
    levels = SponsorLevel.objects.annotate(
        num_sponsors=Count('sponsor')).filter(num_sponsors__gt=0)

    return {
        'levels': levels,
    }
