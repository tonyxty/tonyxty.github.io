import jinja2

AUTHOR = 'Tony Beta Lambda'
SITENAME = 'Lambdaiae'
SITEURL = ""

PATH = "content"
STATIC_PATHS = []

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

SLUGIFY_SOURCE = 'basename'

USE_FOLDER_AS_CATEGORY = False

DEFAULT_DATE_FORMAT = '%Y-%m-%d'
THEME = 'pelican-lambda'

TAGS_URL = "tags"
CATEGORIES_URL = "categories"
ARCHIVES_URL = "archives"
SEARCH_URL = "search"
ARTICLE_LANG_URL = "{slug}.{lang}"
ARTICLE_LANG_SAVE_AS = ARTICLE_LANG_URL + ".html"
PAGE_URL = "{slug}"
PAGE_SAVE_AS = PAGE_URL + ".html"

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {'toc_depth': 2},
        'markdown.extensions.sane_lists': {},
    },
    'output_format': 'html5',
}

JINJA_ENVIRONMENT = {
    'trim_blocks': True,
    'lstrip_blocks': True,
    'undefined': jinja2.StrictUndefined,
}
