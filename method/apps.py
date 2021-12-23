from django.apps import apps, AppConfig
from django.utils.module_loading import autodiscover_modules


class MethodConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'method'
    verbose_name = "测试方法"

    def ready(self):
        autodiscover_modules("adminpro")
