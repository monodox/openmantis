import os
import httpx


def create_foundry_runtime(options=None):
    '''Create a Foundry Local runtime adapter.'''
    options = options or {}
    base_url = options.get('base_url', os.environ.get('OPENMANTIS_RUNTIME_FOUNDRY_URL', 'http://localhost:3000'))
    http_client = options.get('http_client')

    def chat(request):
        client = http_client or httpx.Client()
        try:
            response = client.post(
                f'{base_url}/v1/chat/completions',
                json={
                    'model': request.get('model'),
                    'messages': request.get('messages', []),
                    'max_tokens': request.get('max_output_tokens'),
                    'stream': False,
                },
            )
            response.raise_for_status()
            data = response.json()
            choices = data.get('choices', [])
            content = ''
            if choices:
                content = (choices[0].get('message') or {}).get('content', '')
            return {
                'content': content,
                'raw': data,
            }
        finally:
            if not http_client:
                client.close()

    return {'chat': chat}
