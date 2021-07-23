from django.shortcuts import render, redirect
from django.views import View
from ..models import Course, Video, UserCourse

class CourseView(View):

    def get(self, request, slug):
        course = Course.get_course_by_slug(slug)
        serial_no = request.GET.get('sr_no')
        videos = course.video_set.all().order_by('-serial_number')
        if not serial_no:
            serial_no = 1
        video = Video.objects.get(serial_number= serial_no , course=course)

        if video.is_preview == False:

            if not request.user.is_authenticated :
                return redirect('login')
            else:
                user = request.user
                try:
                    usercourse = UserCourse.objects.get(user=user, course= course)
                except:
                    return redirect('checkout_page', slug= course.slug)
        print(video)
        context = {'course': course, 'video': video, 'videos': videos}
        return render(request, 'courses/course_page.html', context)