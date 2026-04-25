from openmantis.core.cache import create_cache, create_cache_key
from openmantis.core.memory import create_memory_store
from openmantis.core.directory import index_directory
from openmantis.core.router import create_router
from openmantis.core.tokenizer import estimate_tokens, count_message_tokens
from openmantis.runtimes.ollama import create_ollama_runtime
from openmantis.runtimes.foundry import create_foundry_runtime
from openmantis.platform.paths import get_project_root, get_cache_directory, resolve_cache_file
from openmantis.platform.process import get_process_snapshot, read_env_flag, read_env_number
from openmantis.platform.hardware import get_hardware_snapshot, get_memory_gib


def create_openmantis(options=None):
    '''Create an OpenMantis client instance.'''
    options = options or {}

    cache = options.get('cache') or create_cache(options.get('cache_options', {}))
    runtimes = options.get('runtimes') or {
        'ollama': create_ollama_runtime(options.get('ollama_options', {})),
        'foundry': create_foundry_runtime(options.get('foundry_options', {})),
    }

    router = options.get('router') or create_router({
        'cache': cache,
        'runtimes': runtimes,
        'default_runtime': options.get('default_runtime'),
        'max_context_tokens': options.get('max_context_tokens'),
        'max_output_tokens': options.get('max_output_tokens'),
    })

    memory = options.get('memory') or create_memory_store(options.get('memory_options', {}))

    def chat(messages, **kwargs):
        request = {'messages': messages, **kwargs}
        return router.chat(request)

    return {
        'cache': cache,
        'memory': memory,
        'router': router,
        'chat': chat,
    }


__all__ = [
    'create_openmantis',
    'create_cache',
    'create_cache_key',
    'create_memory_store',
    'index_directory',
    'create_router',
    'estimate_tokens',
    'count_message_tokens',
    'create_ollama_runtime',
    'create_foundry_runtime',
    'get_project_root',
    'get_cache_directory',
    'resolve_cache_file',
    'get_process_snapshot',
    'read_env_flag',
    'read_env_number',
    'get_hardware_snapshot',
    'get_memory_gib',
]
