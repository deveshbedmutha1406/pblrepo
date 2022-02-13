from django.contrib import admin
from django.db import models
from .models import Applications, WorkType, Work

@admin.register(Applications)
class ApplicationsAdmin(admin.ModelAdmin):
    list_display = ["user", "contact_no", "type"]

@admin.register(WorkType)
class WorkTypeAdmin(admin.ModelAdmin):
    list_display = ["TypeOfWork"]

admin.site.register(Work)