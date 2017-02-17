from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^results-by-mechanics', views.length_of_service_by_mechanic, name='all_results_by_mechanic'),
    url(r'^results-by-repair-type', views.length_of_service_by_repair_type, name='all_results_by_repair_type'),
    url(r'^$', views.index, name='index'),
]
