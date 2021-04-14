from django.urls import path
from . import views

urlpatterns = [
    path('', views.mycourse, name='Courses'),
    path('<int:id>', views.mycourse_details, name='course_details'),
]
