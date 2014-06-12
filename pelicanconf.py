#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

AUTHOR = u'Elliot Marsden'
SITENAME = u'Small Bangs'

SITEURL = ''

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/elmo.marsden'),
          ('Twitter', 'https://twitter.com/EddieJessup'),
          ('Work', 'http://www.ph.ed.ac.uk/people/elliot-marsden'),
          ('GitHub', 'https://github.com/eddiejessup'),
          )

GITHUB_URL = 'https://github.com/eddiejessup'
TWITTER_URL = 'https://twitter.com/EddieJessup'
FACEBOOK_URL = 'https://www.facebook.com/elmo.marsden'

DEFAULT_PAGINATION = 10

home = os.path.expanduser('~')

THEME = os.path.join(home, 'Pelican/pelican-themes/gum')

PLUGIN_PATH = os.path.join(home, 'Pelican/pelican-plugins')
PLUGINS = ['render_math']

STATIC_PATHS = ['images', 'files']

TYPOGRIFY = True
MD_EXTENSIONS = ['codehilite', 'extra', 'smarty', 'textalign']
