from django.contrib import admin
from .models import Project, Dashboard, ProjectMembership

admin.site.register(Project)
admin.site.register(Dashboard)
admin.site.register(ProjectMembership)