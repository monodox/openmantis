import tempfile

import pytest

from openmantis.core.cache import create_cache
from openmantis.core.router import create_router


def test_router_selects_runtime_and_caches():
    calls = {'count': 0}

    with tempfile.TemporaryDirectory(prefix='openmantis-router-') as directory:
        cache = create_cache({'directory': directory})

        def mock_chat(request):
            calls['count'] += 1
            return {'content': f"reply:{request['messages'][0]['content']}"}

        router = create_router({
            'cache': cache,
            'runtimes': {
                'ollama': {'chat': mock_chat},
            },
        })

        first = router['chat']({'messages': [{'role': 'user', 'content': 'hello'}]})
        second = router['chat']({'messages': [{'role': 'user', 'content': 'hello'}]})

        assert calls['count'] == 1
        assert first['cached'] is False
        assert second['cached'] is True
        assert second['content'] == 'reply:hello'


def test_router_rejects_over_budget():
    router = create_router({
        'cache': None,
        'runtimes': {
            'ollama': {'chat': lambda r: {'content': 'unused'}},
        },
        'max_context_tokens': 1,
    })

    with pytest.raises(RuntimeError, match='Prompt exceeds context budget'):
        router['chat']({'messages': [{'role': 'user', 'content': 'This is definitely too long'}]})
