from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = {
	path('get/<str:actor_name>', views.get, name='get_actor'),
}

urlpatterns = format_suffix_patterns(urlpatterns)
