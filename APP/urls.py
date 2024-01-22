from django.urls import path
from .views import *
urlpatterns = [  
   path('student/', StudentDetail.as_view(), name='studentdetail'),
   path('student/<int:id>/', StudentInfo.as_view(), name='studentinfo'),

]
