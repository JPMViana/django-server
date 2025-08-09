from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Dashboard(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='dashboards')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ProjectMembership(models.Model):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        EDITOR = 'EDITOR', 'Editor'
        VIEWER = 'VIEWER', 'Viewer'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_memberships')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='memberships')
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.VIEWER)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'project')

    def __str__(self):
        return f'{self.user.username} in {self.project.name} as {self.get_role_display()}'