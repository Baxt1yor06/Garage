from django.urls import path
from .views import index,contact,latestDetail,FEATURE

urlpatterns = [
    path('', index, name='index'),
    path('contact',contact,name='contact'),
    path('latesDetial/<int:id>/',latestDetail,name='latestDetail'),
    path('feature/<int:id>/', FEATURE ,name='feature'),
]