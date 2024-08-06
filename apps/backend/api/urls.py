from django.urls import path
from .views import agentDatabaseView

urlpatterns = [
	path('agents', agentDatabaseView.as_view()),
]
