#!/usr/bin/env python
# -*- coding: utf-8 -*- #


from os.path import join, expanduser

AUTHOR = 'Elliot Marsden'
SITENAME = 'Small Bangs'

SITEURL = ''

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/elmo.marsden'),
          ('GitHub', 'https://github.com/eddiejessup'),
          ('Twitter', 'https://twitter.com/EddieJessup'),
          ('Academic', 'http://www.ph.ed.ac.uk/people/elliot-marsden'),
          )

GITHUB_URL = 'https://github.com/eddiejessup'
TWITTER_URL = 'https://twitter.com/EddieJessup'
FACEBOOK_URL = 'https://www.facebook.com/elmo.marsden'

DEFAULT_PAGINATION = 10

home = expanduser('~')

THEME = join(home, 'Desktop/pelican-themes/gum')

PLUGIN_PATHS = [join(home, 'Desktop/pelican-plugins')]
PLUGINS = ['render_math']

STATIC_PATHS = ['images', 'files']

TYPOGRIFY = True
MD_EXTENSIONS = ['codehilite', 'extra', 'smarty', 'textalign']

MENUITEMS = [('Homepage', 'www.elliotmarsden.com')]
