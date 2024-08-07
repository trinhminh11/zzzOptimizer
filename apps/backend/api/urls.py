from django.urls import path
from .views import agentView

urlpatterns = [
	path('agents/', agentView),
]
