from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^get-all-results', views.calculate_length_of_service, name='all_results'),
    url(r'^$', views.index, name='index'),
]
