from django.urls import path,include
from . import views

urlpatterns = [
    path('add_category/' , views.add_categorys , name='add_category'),
]
