from django.apps import apps, AppConfig
from django.utils.module_loading import autodiscover_modules
class SampleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sample'
    verbose_name = "样品管理"

    def ready(self):
        autodiscover_modules("adminpro")

