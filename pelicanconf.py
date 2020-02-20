#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import sys
import os

sys.path.append(os.curdir)
from mesa.mesaconf import *

# TEMPLATE
OWNER = "rwev"
AUTHOR = OWNER
SITENAME = "coyote.life"

SITEURL = "localhost:8000"

SITE_LOGO_URL = "assets/images/geo-yote.png"
TAGLINE = "Live wild or die."

DISPLAY_PAGES_ON_MENU = True
# BUILD PROCESS
DEFAULT_METADATA = {
    "author": OWNER,
    "status": "draft",  # status: published, draft, hidden
}

PATH = "content"
PAGE_PATHS = ["pages"]
STATIC_PATHS = ["assets"]

EXTRA_PATH_METADATA = {
    'assets/extra/robots.txt': {'path': 'robots.txt'},
    'assets/extra/favicon.ico': {'path': 'favicon.ico'},
    'assets/extra/keybase.txt': {'path': 'keybase.txt'}
}

ARTICLE_PATHS = ["articles/published"]
OUTPUT_PATH = "./public"  # for gitlab page

TIMEZONE = "America/Denver"
DEFAULT_LANG = "en"

# PLUGINS
PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = [
    "filetime_from_git",
    "autopages",
    "similar_posts",
    "neighbors",
    "section_number",
    "more_categories",
    "gzip_cache",
    "photos",
    "summary",
    "sitemap"
]

# autopages
AUTOPAGES_PATH = os.path.join("content", "autopages")

AUTHOR_PAGE_PATH = os.path.join(AUTOPAGES_PATH, "authors")
CATEGORY_PAGE_PATH = os.path.join(AUTOPAGES_PATH, "categories")
TAG_PAGE_PATH = os.path.join(AUTOPAGES_PATH, "tags")

# deadlinks
DEADLINK_OPTS = {
    'archive':  True,
    'classes': [], # TODO
    'labels':   False,
    'timeout_duration_ms': 1000,
    'timeout_is_error':    True,
}

# photos
PHOTO_LIBRARY = "./content/assets/images"
PHOTO_EXIF_COPYRIGHT_AUTHOR = "Ryan William"

# 1.33~ width / height ratio
# (width, height, quality % of max)
PHOTO_GALLERY = (2000, 1500, 95)
PHOTO_ARTICLE = (760, 506, 95)
PHOTO_THUMB = (300, 225, 70)

# sitemap
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.9,
        "pages": 0.8,
        "indexes": 0.7,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly"
    }
}

