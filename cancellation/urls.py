from django.conf.urls import url  
from . import views
from django.urls import path
app_name = 'cancellation'


urlpatterns = [
    path('', views.cancellation_view, name='cancellation'),
    path('<slug>', views.cancel, name='try')
]
