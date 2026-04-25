import os
import platform
import sys
import time


def get_process_snapshot():
    '''Return a snapshot of the current process.'''
    try:
        import psutil
        proc = psutil.Process(os.getpid())
        uptime = int(time.time() - proc.create_time())
        avail = psutil.virtual_memory().available
    except ImportError:
        uptime = 0
        avail = 0

    return {
        'pid': os.getpid(),
        'ppid': os.getppid(),
        'platform': sys.platform,
        'arch': platform.machine(),
        'cwd': os.getcwd(),
        'python_version': sys.version,
        'uptime_seconds': uptime,
        'available_memory_bytes': avail,
    }


def read_env_flag(name, fallback=False, env=None):
    '''Read a boolean flag from an environment variable.'''
    env = env if env is not None else os.environ
    value = env.get(name)
    if value is None:
        return fallback
    return str(value).lower() in ('1', 'true', 'yes', 'on')


def read_env_number(name, fallback=0, env=None):
    '''Read a numeric value from an environment variable.'''
    env = env if env is not None else os.environ
    value = env.get(name)
    if value is None or value == '':
        return fallback
    try:
        parsed = float(value)
        if parsed != parsed:  # NaN check
            return fallback
        return int(parsed) if parsed == int(parsed) else parsed
    except (ValueError, OverflowError):
        return fallback
