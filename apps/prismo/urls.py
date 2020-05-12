from django.conf.urls import url
from . import views 

urlpatterns=[
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^dashboard$', views.dashboard),
    url(r'^edit_profile/(?P<user_id>\d+)$', views.edit_profile),
    url(r'^post_status/(?P<user_id>\d+)$' , views.post_status),
    url(r'^like_status/(?P<post_id>\d+)$' , views.like_status),
    url(r'^post_comment/(?P<post_id>\d+)$' , views.post_comment),
    url(r'^delete_comment/(?P<post_id>\d+)$', views.delete_comment),
    
]