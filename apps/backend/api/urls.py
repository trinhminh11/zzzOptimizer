from django.urls import path
from .views import test, agentModelView, agentView


urlpatterns = [
	path('agents/', agentModelView.as_view()),
	# path('agents/', agentView),
	path('test/', test)
]
