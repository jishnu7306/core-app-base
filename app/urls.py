from django.urls import re_path
from .import views


urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^reportedissue$', views.reportedissue, name='reportedissue'),
    re_path(r'^reportissue$', views.reportissue, name='reportissue'),
    re_path(r'^reportedissuesub$', views.reportedissuesub, name='reportedissuesub'),
    re_path(r'^applyleave$', views.applyleave, name='applyleave'),
    re_path(r'^applyleavesub$', views.applyleavesub, name='applyleavesub')
]
