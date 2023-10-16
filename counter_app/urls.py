# counter_app/urls.py

from django.urls import path
from . import views

app_name = 'counter'
urlpatterns = [
    path('', views.counter, name='counter'),
    path('increment/<int:counter_id>/', views.increment, name='increment'),
    path('reset/<int:counter_id>/', views.reset, name='reset'),
    path('save/', views.save, name='save'),
    path('<int:counter_id>/', views.counter_detail, name='counter_detail'),
]
