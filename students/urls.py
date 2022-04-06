from django.conf.urls import url
from students import views

urlpatterns = [
    url(r'^alumnos/$', views.StudentList.as_view()),
    url(r'^alumnos/(?P<pk>[0-9]+)/$', views.StudentDetail.as_view()),
]
