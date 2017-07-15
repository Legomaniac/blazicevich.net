#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = "/root/Flex"

SITETITLE = "James Blazicevich"
SITESUBTITLE = "DevOps | Home Automation"

MAIN_MENU = False

AUTHOR = 'James Blazicevich'
SITENAME = 'James Blazicevich'
SITEURL = 'http://blazicevich.net'

STATIC_PATHS = ['static']

EXTRA_PATH_METADATA = { 
    'static/favicon.ico': {'path': 'favicon.ico'} 
}

TIMEZONE = 'America/Denver'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('BozemanBricks', 'http://www.bricklink.com/store.asp?p=MattNJames'),)

# Social widget
SOCIAL = (('github', 'http://github.com/Legomaniac'),
          ('linkedin', 'https://www.linkedin.com/in/james-blazicevich'),
          ('youtube', 'https://www.youtube.com/user/legomaniac/videos'),
          ('envelope-o', 'mailto:james@blazicevich.net'),
)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
