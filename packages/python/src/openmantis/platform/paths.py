import os


def get_project_root(start_directory=None):
    '''Walk up from start_directory to find a directory containing pyproject.toml or package.json.'''
    current = os.path.abspath(start_directory or os.getcwd())

    while True:
        if os.path.exists(os.path.join(current, 'pyproject.toml')):
            return current
        if os.path.exists(os.path.join(current, 'package.json')):
            return current

        parent = os.path.dirname(current)
        if parent == current:
            return os.path.abspath(start_directory or os.getcwd())

        current = parent


def get_cache_directory(env=None, start_directory=None):
    '''Resolve the cache directory path.'''
    env = env if env is not None else os.environ
    start = start_directory or os.getcwd()
    cache_dir = env.get('OPENMANTIS_CACHE_DIR', '.openmantis/cache')
    return os.path.normpath(os.path.join(start, cache_dir))


def resolve_cache_file(file_name='cache.json', env=None, start_directory=None):
    '''Resolve a file path inside the cache directory.'''
    return os.path.join(get_cache_directory(env, start_directory), file_name)
