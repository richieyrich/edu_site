from django.db import models
from django.contrib.auth.models import User
from .course import Course

class UserCourse(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f'{self.user.username}-{self.course.name}'
