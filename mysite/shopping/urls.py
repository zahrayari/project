from django.urls import path
from . import views
from .views import post_list,post_detail

app_name = 'shopping'
urlpatterns = [
 # post views
    path('', post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
    views.post_detail,
    name='post_detail'),
]