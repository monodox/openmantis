import json

from openmantis.runtimes.ollama import create_ollama_runtime
from openmantis.runtimes.foundry import create_foundry_runtime


class MockResponse:
    def __init__(self, data, status_code=200):
        self._data = data
        self.status_code = status_code

    def raise_for_status(self):
        if self.status_code >= 400:
            raise Exception(f'HTTP {self.status_code}')

    def json(self):
        return self._data


class MockClient:
    def __init__(self, response_data):
        self.last_url = None
        self.last_json = None
        self._response = MockResponse(response_data)

    def post(self, url, json=None):
        self.last_url = url
        self.last_json = json
        return self._response

    def close(self):
        pass


def test_ollama_posts_expected_payload():
    client = MockClient({'message': {'content': 'ollama reply'}})
    runtime = create_ollama_runtime({
        'base_url': 'http://example.test',
        'http_client': client,
    })

    response = runtime['chat']({
        'model': 'llama3',
        'messages': [{'role': 'user', 'content': 'hi'}],
    })

    assert client.last_url == 'http://example.test/api/chat'
    assert client.last_json['model'] == 'llama3'
    assert response['content'] == 'ollama reply'


def test_foundry_posts_expected_payload():
    client = MockClient({'choices': [{'message': {'content': 'foundry reply'}}]})
    runtime = create_foundry_runtime({
        'base_url': 'http://example.test',
        'http_client': client,
    })

    response = runtime['chat']({
        'model': 'phi-3.5-mini',
        'messages': [{'role': 'user', 'content': 'hi'}],
        'max_output_tokens': 32,
    })

    assert client.last_url == 'http://example.test/v1/chat/completions'
    assert client.last_json['max_tokens'] == 32
    assert response['content'] == 'foundry reply'
