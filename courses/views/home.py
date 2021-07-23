from django.shortcuts import render, redirect
from django.views import View
from ..models import Course

class Home(View):

    def get(self, request):
        courses = Course.get_all_courses()
        context = {'courses': courses}
        return render(request, 'courses/home.html', context)