#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Shivan Sornarajah'
SITENAME = 'sornars'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEE_RSS = None

# Blogroll
# LINKS = (('Github', 'https://github.com/sornars/'),)

# # Social widget
SOCIAL = (('LinkedIn', 'https://uk.linkedin.com/in/sornars'),
         ('Github', 'https://github.com/sornars/')) 

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = './themes/pelican-blue'

DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives')
SITEMAP_SAVE_AS = 'sitemap.xml'

STATIC_PATHS = ['images', 'extra/robots.txt']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'}
}

DISPLAY_PAGES_ON_MENU = True
MENUITEMS = (('Blog', 'http://www.sornars.com'),)
# Settings for pelican-ipynb
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']
IGNORE_FILES = ['.ipynb_checkpoints']

# Settings for pelican-blue
DISPLAY_FOOTER = False
SIDEBAR_DIGEST = 'Developer, Ad Operations and aspiring Data Scientist'
