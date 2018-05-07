from django.conf.urls import url
from . import views



urlpatterns=[
    url('^$',views.index,name='index'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^imageLocation/(\d+)',views.location,name = 'imageLocation'),
    url(r'^imagecategory/(\d+)',views.imageCategory,name = 'imageCategory'),
    url(r'^imageDetails/(\d+)',views.viewDetails,name = 'imageDetails'),

]

