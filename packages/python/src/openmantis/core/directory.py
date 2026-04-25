import os
from datetime import datetime, timezone


def index_directory(directory, options=None):
    '''Index files in a directory tree, returning metadata for each file.'''
    options = options or {}
    max_depth = options.get('max_depth', float('inf'))
    ignore_names = set(options.get('ignore_names', ['node_modules', '.git', '__pycache__']))
    entries = []

    _walk(directory, 0, max_depth, ignore_names, entries)
    return entries


def _walk(current_directory, depth, max_depth, ignore_names, entries):
    if depth > max_depth:
        return

    if not os.path.isdir(current_directory):
        stat = os.stat(current_directory)
        entries.append(_make_entry(current_directory, stat))
        return

    for entry_name in sorted(os.listdir(current_directory)):
        if entry_name in ignore_names:
            continue

        full_path = os.path.join(current_directory, entry_name)
        stat = os.stat(full_path)

        if os.path.isdir(full_path):
            _walk(full_path, depth + 1, max_depth, ignore_names, entries)
            continue

        entries.append(_make_entry(full_path, stat))


def _make_entry(file_path, stat):
    modified = datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat()
    return {
        'path': file_path,
        'size': stat.st_size,
        'modified_time': modified,
    }
