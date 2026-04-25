import os
import tempfile

from openmantis.core.cache import create_cache, create_cache_key


def test_create_cache_stores_and_retrieves():
    with tempfile.TemporaryDirectory(prefix='openmantis-cache-') as directory:
        cache = create_cache({'directory': directory})
        key = create_cache_key({'hello': 'world'})

        assert cache['has'](key) is False

        cache['set'](key, {'content': 'cached response'})

        assert cache['has'](key) is True
        assert cache['get'](key) == {'content': 'cached response'}
        assert cache['stats']()['entries'] == 1
