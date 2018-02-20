from django.conf.urls import url

from src.core import views as core_views

app_name = 'Core'

urlpatterns = [
    url(r'^$', core_views.home, name='home'),
]
