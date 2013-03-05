try:
    VERSION = __import__('pkg_resources') \
        .get_distribution('django-shortuuidfield').version
except Exception, e:
    VERSION = 'unknown'
    
from fields import ShortUUIDField