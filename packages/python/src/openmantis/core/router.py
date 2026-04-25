from openmantis.core.cache import create_cache_key
from openmantis.core.tokenizer import count_message_tokens


def create_router(options=None):
    '''Create a request router with caching and token budgeting.'''
    options = options or {}
    cache = options.get('cache')
    runtimes = options.get('runtimes', {})
    default_runtime = options.get('default_runtime', 'ollama')
    max_context_tokens = options.get('max_context_tokens', 4096)
    max_output_tokens = options.get('max_output_tokens', 1024)

    def chat(request=None):
        request = request or {}
        normalized = _normalize_request(request, default_runtime, max_output_tokens)
        runtime_name = normalized['runtime']
        runtime = runtimes.get(runtime_name)

        if not runtime or 'chat' not in runtime or not callable(runtime['chat']):
            raise RuntimeError(f'Unknown runtime: {runtime_name}')

        tokens = count_message_tokens(normalized['messages'])
        if tokens > max_context_tokens:
            raise RuntimeError(f'Prompt exceeds context budget: {tokens} > {max_context_tokens}')

        cache_key = create_cache_key({
            'runtime': runtime_name,
            'model': normalized['model'],
            'messages': normalized['messages'],
            'maxOutputTokens': normalized['max_output_tokens'],
        })

        if cache and cache['has'](cache_key):
            result = cache['get'](cache_key)
            result['cached'] = True
            return result

        response = runtime['chat'](normalized)
        result = {**response, 'cached': False, 'runtime': runtime_name}

        if cache:
            cache['set'](cache_key, result)

        return result

    return {'chat': chat}


def _normalize_request(request, default_runtime, max_output_tokens):
    messages = request.get('messages', [])
    return {
        'runtime': request.get('runtime', default_runtime),
        'model': request.get('model'),
        'messages': [_normalize_message(m) for m in messages] if isinstance(messages, list) else [],
        'max_output_tokens': request.get('max_output_tokens', max_output_tokens),
    }


def _normalize_message(message):
    return {
        'role': message.get('role', ''),
        'content': str(message.get('content', '')),
    }
