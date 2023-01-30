import importlib
import os
import time
import inspect
import logging


def init(**kwargs):

    plugins = [
        importlib.import_module(f'.', f'{__name__}.{file[:-3]}')
        for file in os.listdir(os.path.dirname(__file__))
        if file[0].isalpha() and file.endswith('.py')
    ]

    modules = {m.__name__.split('.')[-1]: m for m in plugins}
    for plugin in sorted(plugins, key=lambda x: x.__name__):
        get_init_coro(plugin, modules=modules, **kwargs)


def get_init_coro(plugin, **kwargs):
    p_init = getattr(plugin, 'init', None)
    if not callable(p_init):
        return

    result_kwargs = {}
    sig = inspect.signature(p_init)
    for param in sig.parameters:
        if param in kwargs:
            result_kwargs[param] = kwargs[param]
        else:
            logging.info('Plugin %s has unknown init parameter %s', plugin.__name__, param.__name__)
            return

    return _init_plugin(plugin, result_kwargs)


def _init_plugin(plugin, kwargs):
    try:
        logging.info(f'Loading plugin {plugin.__name__}…')
        start = time.time()
        plugin.init(**kwargs)
        took = time.time() - start
        logging.info(f'Loaded plugin {plugin.__name__} (took {took:.2f}s)')
    except Exception as e:
        logging.error(f'Failed to load plugin {plugin}\n{e}\n\n')
