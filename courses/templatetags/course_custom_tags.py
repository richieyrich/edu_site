from courses.models import usercourse
from django import template
from math import floor
from ..models import UserCourse


register = template.Library()

@register.simple_tag
def cal_sellprice(price, discount):
    if discount is None or discount == 0 :
        return price
    sellprice = price - (price*discount/100)
    return floor(sellprice)


@register.filter
def currency(price):
    return f'₹{price}'

@register.simple_tag
def is_enrolled(request, course):
    if not request.user.is_authenticated:
        return False
    try:
        usercourse = UserCourse.objects.get(user= request.user, course=course)
        return True
    except:
        return False
    return False