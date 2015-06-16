#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Shivan Sornarajah'
SITENAME = 'sornars'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Github', 'https://github.com/sornars/'),)

# # Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

PROJECTS = (('www.sornars.com', 'https://github.com/sornars/www.sornars.com', 'This blog!'),
            ('Taxi Trajectory Prediction (I)', 
             'https://github.com/sornars/pkdd_15_predict_taxi_service_trajectory_i', 
             'Kaggle.com competition entry to predict taxi destinations given partial trajectories.'),
            ('Dotfiles', 
             'https://github.com/sornars/dotfiles', 
             'Personal dotfiles stored on Github for easy setup on new machines.'),
            ('Bike Sharing Demand', 
             'https://github.com/sornars/bike_sharing_demand', 
             'Kaggle.com competition entry to predict the number of bicycles that will be rented on a given day in Washington, D.C.'),
            ('Open Source Contributions', 
             'https://github.com/pulls?q=is%3Apr+author%3Asornars+is%3Aclosed', 
             'Various patches to different projects including scikit-learn, urllib3 and astropy.'),) 

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = './themes/dev-random2-en'

DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'sitemap', 'portfolio')
SITEMAP_SAVE_AS = 'sitemap.xml'

STATIC_PATHS = ['images', 'extra/robots.txt']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'}
}

# Settings for pelican-ipynb
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb']
