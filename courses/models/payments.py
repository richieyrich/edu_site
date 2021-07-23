
from django.db import models
from django.contrib.auth.models import User
from . import Course, UserCourse



class Payments(models.Model):
    order_id = models.CharField(max_length=50, null=False, blank=True)
    payment_id = models.CharField(max_length=50, null=True, unique=True)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)
    user_course = models.ForeignKey(UserCourse, null=True, blank=True, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    
