from django.shortcuts import render, get_object_or_404
from PortFolio .models import Course
from .models import MyCourse
# Create your views here.
def mycourse(request):
    all_courses = Course.objects.all()
    data = {
        'all_courses' : all_courses
    }
    return render(request, 'myCourses/mycourse.html', data)




def mycourse_details(request, id):
    feature_courses = get_object_or_404(MyCourse, pk=id)
    data = {
        'feature_courses':feature_courses
    }
    return render(request, 'myCourses/course_detail.html', data)
