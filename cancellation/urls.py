from django.conf.urls import url  
from . import views
from django.urls import path
app_name = 'cancellation'


urlpatterns = [
    path('cancellation/', views.cancellation_view, name='cancellation')
]
print('hello\n'*100)