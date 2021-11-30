from django.contrib import admin

from .models import Project

# Register your models here.
#mostrar los campos que son solo de lectura en admin al crear un proyecto
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(Project, ProjectAdmin)