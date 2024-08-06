from django.urls import path
from .views import main, init

urlpatterns = [
	path('', main),
]
