from django.apps import apps, AppConfig
from django.contrib import admin
models_dict = {}

class ListAdminMixin(object):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        # self.list_verbose_name = [field.verbose_name for field in model._meta.fields]
        # print(self.list_verbose_name)
        super(ListAdminMixin, self).__init__(model, admin_site)


class UniversalManagerApp(AppConfig):
    name = "ChemistryLIMS"
    auto_app_list = ['equipment', 'evr', 'method', 'sample', 'product', 'document']

    def ready(self):
        for item in self.auto_app_list:
            models = apps.get_app_config(item).get_models()
            for model in models:
                models_dict[model._meta.model_name] = model
                admin_name = model.__name__ + "Admin"
                admin_class = type(admin_name, (ListAdminMixin, admin.ModelAdmin), {})
                try:
                    admin.site.register(model, admin_class)
                except admin.sites.AlreadyRegistered:
                    pass
