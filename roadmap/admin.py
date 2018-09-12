from django.contrib import admin

# Register your models here.
from roadmap.models import Step, Roadmap, Project

admin.site.register(Step)
admin.site.register(Roadmap)
admin.site.register(Project)
