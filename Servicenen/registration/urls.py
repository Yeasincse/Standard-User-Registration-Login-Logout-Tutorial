from django.conf.urls import url
from registration import views

urlpatterns = [
    url(r'^register/$',views.register_user,name='register_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^login_user/$',views.login_user,name='login_user'),
]
