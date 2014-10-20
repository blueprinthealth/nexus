from . import autodiscover

try:
    from django.apps import AppConfig
except ImportError:
    pass
else:
    class NexusConfig(AppConfig):
        name = 'nexus'

        def ready(self):
            autodiscover()
