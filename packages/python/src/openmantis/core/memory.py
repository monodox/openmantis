import json
import os


def create_memory_store(options=None):
    '''Create a persistent key-value memory store.'''
    options = options or {}
    file_path = options.get('file_path', os.path.join(os.getcwd(), '.openmantis', 'memory.json'))

    _ensure_parent_directory(file_path)

    def get(key):
        state = _read_state(file_path)
        return state['entries'].get(key)

    def set_(key, value):
        state = _read_state(file_path)
        state['entries'][key] = value
        _write_state(file_path, state)
        return value

    def has(key):
        state = _read_state(file_path)
        return key in state['entries']

    def delete(key):
        state = _read_state(file_path)
        existed = key in state['entries']
        state['entries'].pop(key, None)
        _write_state(file_path, state)
        return existed

    def list_keys():
        state = _read_state(file_path)
        return list(state['entries'].keys())

    def clear():
        _write_state(file_path, {'entries': {}})

    return {
        'get': get,
        'set': set_,
        'has': has,
        'delete': delete,
        'list': list_keys,
        'clear': clear,
    }


def _ensure_parent_directory(file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)


def _read_state(file_path):
    if not os.path.exists(file_path):
        return {'entries': {}}

    with open(file_path, 'r', encoding='utf-8') as f:
        raw = f.read().strip()

    if not raw:
        return {'entries': {}}

    return json.loads(raw)


def _write_state(file_path, state):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(state, indent=2) + '\n')
