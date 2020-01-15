from __future__ import unicode_literals
from django.contrib import admin
from .models import *

from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Register your models here.


class TodoListAdmin(admin.ModelAdmin):
    list_display = ("title",  "created", "due_date")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


class WeddingDayAdmin(admin.ModelAdmin):
    list_display = ('time', 'item', 'notes')


admin.site.register(TodoList)
admin.site.register(Category)
admin.site.register(WeddingDay)
admin.site.register(Coordinator)







# class CoordinationResource(resources.ModelResource):
#     class Meta:
#         model = Coordinator
#         exclude = ('id',)
#         fields = ('name', 'role', 'phone', 'email', 'website', 'cost', 'notes')
#
# @admin.register(Coordinator)
# class ViewAdmin(ImportExportModelAdmin):
#     resources_class = CoordinationResource
#     exclude = ('id',)