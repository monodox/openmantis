import os
import tempfile

from openmantis.core.directory import index_directory
from openmantis.core.memory import create_memory_store
from openmantis.platform.paths import get_cache_directory, resolve_cache_file
from openmantis.platform.process import read_env_flag, read_env_number


def test_index_directory_skips_ignored():
    with tempfile.TemporaryDirectory(prefix='openmantis-dir-') as root:
        os.makedirs(os.path.join(root, 'nested'))
        os.makedirs(os.path.join(root, 'node_modules'))

        with open(os.path.join(root, 'alpha.txt'), 'w') as f:
            f.write('alpha')
        with open(os.path.join(root, 'nested', 'beta.txt'), 'w') as f:
            f.write('beta')
        with open(os.path.join(root, 'node_modules', 'ignored.txt'), 'w') as f:
            f.write('ignored')

        entries = index_directory(root)

        paths = [e['path'] for e in entries]
        assert not any('ignored.txt' in p for p in paths)
        assert any(p.endswith('alpha.txt') for p in paths)
        assert any(p.endswith('beta.txt') for p in paths)


def test_memory_store_persists():
    with tempfile.TemporaryDirectory(prefix='openmantis-memory-') as d:
        file_path = os.path.join(d, 'memory.json')
        memory = create_memory_store({'file_path': file_path})

        assert memory['has']('note') is False
        memory['set']('note', {'text': 'remember this'})
        assert memory['has']('note') is True
        assert memory['get']('note') == {'text': 'remember this'}
        assert memory['list']() == ['note']


def test_cache_directory_resolves():
    with tempfile.TemporaryDirectory(prefix='openmantis-root-') as root:
        result = get_cache_directory({'OPENMANTIS_CACHE_DIR': 'custom/cache'}, root)
        assert result == os.path.normpath(os.path.join(root, 'custom/cache'))


def test_resolve_cache_file():
    with tempfile.TemporaryDirectory(prefix='openmantis-root-') as root:
        result = resolve_cache_file('state.json', {'OPENMANTIS_CACHE_DIR': 'custom/cache'}, root)
        expected = os.path.join(os.path.normpath(os.path.join(root, 'custom/cache')), 'state.json')
        assert result == expected


def test_read_env_flag():
    assert read_env_flag('TEST_FLAG', False, {'TEST_FLAG': 'yes'}) is True
    assert read_env_flag('TEST_FLAG', True, {}) is True


def test_read_env_number():
    assert read_env_number('TEST_NUM', 7, {'TEST_NUM': '42'}) == 42
    assert read_env_number('TEST_NUM', 7, {}) == 7
