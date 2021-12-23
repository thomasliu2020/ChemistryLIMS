from django.contrib import admin
from .models import *
from import_export.admin import ImportExportActionModelAdmin
from ChemistryLIMS.apps import ListAdminMixin


# Register your models here.

class TestLogInline(admin.TabularInline):
    model = TestLog
    fields = ('item', 'method', 'result', 'unit', 'spec', 'date', 'chemist', 'type',)
    extra = 0


@admin.register(SampleLog)
class SampleLogAdmin(ListAdminMixin, ImportExportActionModelAdmin):
    inlines = [TestLogInline]

    def get_search_fields(self, request):
        return self.model.search_fields

    def get_list_filter(self, request):
        return self.model.list_filter
