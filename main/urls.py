from django.urls import path
from . import views 



urlpatterns = [
    path('' , views.index , name="index" ),
    path('main_admin/' , views.main_admin , name="main_admin" ),
    path('getdata/' , views.getdata , name="getdata" ),
    path('login/' , views.login , name="login" ),
    # path('postsubmit/' , views.postsubmit , name="postsubmit" ),
]