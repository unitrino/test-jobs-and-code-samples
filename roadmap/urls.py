from django.urls import path
from roadmap.views import ProjectViewSet, DashboadTemplate

urlpatterns = [
    path('dashboard/', DashboadTemplate.as_view(), name='dashboard'),
    path('api/projects', ProjectViewSet.as_view({'get': 'list'}), name='dashboard')
]