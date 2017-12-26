from django.conf.urls import url
from newapp import views

urlpatterns = [
    #url(r'index/',views.index,name='index'),
    url(r'result/',views.assessmentForm,name='result'),
    url(r'country/',views.getUniversityList,name='getUniversityList'),
    url(r'highCountry/',views.highCountry,name='highCountry'),
    url(r'index/',views.index,name='index'),
    url(r'highResult/', views.highResult,name='highResult'),
    url(r'highResultUK/', views.highResultUK, name='highResultUK'),
    url(r'highResultCA/', views.highResultCA, name='highResultCA'),
]