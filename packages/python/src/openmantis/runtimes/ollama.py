import os
import httpx


def create_ollama_runtime(options=None):
    '''Create an Ollama runtime adapter.'''
    options = options or {}
    base_url = options.get('base_url', os.environ.get('OPENMANTIS_RUNTIME_OLLAMA_URL', 'http://localhost:11434'))
    http_client = options.get('http_client')

    def chat(request):
        client = http_client or httpx.Client()
        try:
            response = client.post(
                f'{base_url}/api/chat',
                json={
                    'model': request.get('model'),
                    'messages': request.get('messages', []),
                    'stream': False,
                },
            )
            response.raise_for_status()
            data = response.json()
            return {
                'content': (data.get('message') or {}).get('content', ''),
                'raw': data,
            }
        finally:
            if not http_client:
                client.close()

    return {'chat': chat}
