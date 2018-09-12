from django.views.generic import TemplateView
from rest_framework import viewsets
from roadmap.models import Project
from roadmap.serializers import ProjectSerializer


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class DashboadTemplate(TemplateView):
    template_name = "dashboard/dashboard.html"
