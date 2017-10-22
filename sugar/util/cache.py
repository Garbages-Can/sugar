from threading import local


class InvalidCacheError(Exception):
    pass


class CacheKeyWarning(RuntimeWarning):
    pass


class DefaultCache():
    """
    the cache base class, this makes it easy to expand in the future.

    thread safety
    """

    def __init__(self):
        self.cache = local()

    def __setitem__(self, key, value):
        try:
            self.cache.caches[key] = value
        except Exception:
            self.cache.caches = {key: value}

    def __getitem__(self, item):
        try:
            return self.cache.caches[item]
        except AttributeError:
            self.cache.caches = {}
        except Exception:
            pass

    def __contains__(self, item):
        try:
            return item in self.cache.caches
        except Exception:
            return False

    def __repr__(self):
        try:
            return repr(self.cache.caches)
        except:
            return "Cache: None"


cache = DefaultCache()
