from django.urls import re_path
from .import views


urlpatterns = [
    re_path(r'^$', views.index, name='index'),

    ########## Reprt issue
    #Jishnu
    re_path(r'^reportedissue$', views.reportedissue, name='reportedissue'),
    re_path(r'^reportissue$', views.reportissue, name='reportissue'),
    re_path(r'^reportedissuesub$', views.reportedissuesub, name='reportedissuesub'),

    #saneesha
    re_path(r'^reportissuetrainers$', views.reportissuetrainers, name='reportissuetrainers'),
    re_path(r'^reportissuetrainees$', views.reportissuetrainees, name='reportissuetrainees'),
    re_path(r'^trainerunsolvedissue$', views.trainerunsolvedissue, name='trainerunsolvedissue'),
    re_path(r'^trainersolvedissue$', views.trainersolvedissue, name='trainersolvedissue'),
    re_path(r'^traineesunsolved$', views.traineesunsolved, name='traineesunsolved'),
    re_path(r'^traineessolved$', views.traineessolved, name='traineessolved'),

    



    ############ Apply leave
    #jishnu
    re_path(r'^applyleave$', views.applyleave, name='applyleave'),
    re_path(r'^applyleavesub$', views.applyleavesub, name='applyleavesub'),
 
    #Seban
    re_path(r'^Requestedleave$', views.Requestedleave, name='Requestedleave'),    

    #Althaf   
    re_path(r'^trainers_leave$', views.trainers_leave, name='trainers_leave'),
    re_path(r'^trainees_leave$', views.trainees_leave, name='trainees_leave'),
]
