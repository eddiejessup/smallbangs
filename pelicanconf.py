#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Elliot Marsden'
SITENAME = u'Small Bangs'
SITEURL = ''

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         )

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/elmo.marsden'),
          ('Twitter', 'https://twitter.com/EddieJessup'),
          ('Work', 'http://www.ph.ed.ac.uk/people/elliot-marsden'),
          ('GitHub', 'https://github.com/eddiejessup'),
          )

DEFAULT_PAGINATION = 10

THEME = "/Users/ejm/Projects/SmallBangs/pelican-themes/bootstrap"

PLUGIN_PATH = '/Users/ejm/Projects/SmallBangs/pelican-plugins'
PLUGINS = ['render_math']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
