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
SOCIAL = (
    ('GitHub', 'https://github.com/eddiejessup'),
    ('Twitter', 'https://twitter.com/EddieJessup'),
)

GITHUB_URL = 'https://github.com/eddiejessup'
TWITTER_URL = 'https://twitter.com/EddieJessup'

DEFAULT_PAGINATION = 10

THEME = 'pelican-themes/gum'

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['render_math', 'liquid_notebooks.notebook']

TYPOGRIFY = False
MD_EXTENSIONS = ['codehilite', 'extra', 'smarty', 'textalign']

MENUITEMS = [
    ('Non-blog', '//elliotmarsden.com')
]

MARKUP = ('md', 'ipynb')
