import hashlib
import json
import os


def create_cache(options=None):
    '''Create a disk-backed cache store.'''
    options = options or {}
    directory = options.get('directory', os.path.join(os.getcwd(), '.openmantis', 'cache'))
    file_path = os.path.join(directory, 'cache.json')

    _ensure_directory(directory)

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

    def clear():
        _write_state(file_path, {'entries': {}})

    def stats():
        state = _read_state(file_path)
        return {
            'directory': directory,
            'entries': len(state['entries']),
        }

    return {
        'get': get,
        'set': set_,
        'has': has,
        'delete': delete,
        'clear': clear,
        'stats': stats,
    }


def create_cache_key(payload):
    '''Generate a SHA-256 cache key from a payload dict.'''
    raw = json.dumps(payload, sort_keys=True, separators=(',', ':'))
    return hashlib.sha256(raw.encode('utf-8')).hexdigest()


def _ensure_directory(directory):
    os.makedirs(directory, exist_ok=True)


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
