import os
import platform


def get_hardware_snapshot():
    '''Return a snapshot of the current hardware.'''
    try:
        import psutil
        total = psutil.virtual_memory().total
        free = psutil.virtual_memory().available
    except ImportError:
        total = 0
        free = 0

    return {
        'cpu_count': os.cpu_count() or 1,
        'total_memory_bytes': total,
        'free_memory_bytes': free,
        'platform': platform.system().lower(),
        'architecture': platform.machine(),
    }


def get_memory_gib(byte_count):
    '''Convert bytes to GiB, rounded to 2 decimal places.'''
    return round(byte_count / (1024 ** 3), 2)
