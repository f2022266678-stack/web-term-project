from django.contrib import admin
from .models import Skill

# Register your models here.

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency', 'category')
    list_filter = ('category',)
    search_fields = ('name',)
