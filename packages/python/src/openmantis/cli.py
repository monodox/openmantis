import json
import sys

from openmantis import create_openmantis


def main():
    '''CLI entrypoint for openmantis.'''
    argv = sys.argv[1:]

    if not argv or argv[0] == 'run':
        args = argv[1:] if argv and argv[0] == 'run' else argv
        return run_command(args)

    if argv[0] == 'status':
        return status_command()

    if argv[0] == 'cache':
        return cache_command()

    print(f'Unknown command: {argv[0]}', file=sys.stderr)
    sys.exit(1)


def run_command(argv):
    '''Execute a prompt against a local runtime.'''
    prompt = ' '.join(argv).strip()
    if not prompt:
        print('Provide a prompt to run', file=sys.stderr)
        sys.exit(1)

    client = create_openmantis()
    response = client['chat'](messages=[{'role': 'user', 'content': prompt}])
    print(response.get('content', ''))
    return response


def status_command():
    '''Print cache stats.'''
    client = create_openmantis()
    stats = client['cache']['stats']()
    print(json.dumps(stats, indent=2))
    return stats


def cache_command():
    '''Print cache stats.'''
    client = create_openmantis()
    stats = client['cache']['stats']()
    print(json.dumps(stats, indent=2))
    return stats
