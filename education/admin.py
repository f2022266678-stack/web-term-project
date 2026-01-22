from django.contrib import admin
from .models import Education

# Register your models here.

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree_title', 'institution', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date')
    search_fields = ('degree_title', 'institution')
