from os import error
from courses.models import course, usercourse
from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from ..models import Course, Payments, UserCourse
from django.conf import settings
from time import time
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

import razorpay
client = razorpay.Client(auth=(settings.KEY_ID , settings.KEY_SECRET))

class CheckoutView(View):

    def get(self, request, slug):
        course = Course.get_course_by_slug(slug)
        action = request.GET.get('action')
        user = None
        order = None
        payment = None
        error = None

        if ( not request.user.is_authenticated ) :
            return redirect('login')
        user = request.user
        
        if action== 'create_payment':
            try:
                usercourse = UserCourse.objects.get(user=user, course= course)
                error = ' u r already enrolled'
            except:
                pass
            if error is None: 
                amount = int((course.price - (course.price*course.discount/100))*100)
                currency = 'INR'
                receipt = f'rec{int(time())}'
                notes = {
                    'email': user.email,
                    'name': f'{user.first_name} {user.last_name}'
                }
                order = client.order.create({'amount': amount , 'currency': currency, 'receipt': receipt, 'notes': notes })
                payment = Payments()
                payment.course = course
                payment.user = user
                payment.order_id = order.get('id')
                payment.save()
        
        context = {'course': course, 'order':order, 'payment': payment, 'user': user, 'error': error}
        return render(request, 'courses/checkout.html', context)


@method_decorator(csrf_exempt, name='dispatch')
class PaymentSuccess(View):
    
    def post(self, request):
        data = request.POST
        try:
            client.utility.verify_payment_signature(data)
            order_id = data['razorpay_order_id']
            payment_id = data['razorpay_payment_id']
            payment = Payments.objects.get(order_id=order_id)
            payment.payment_id = payment_id
            payment.status = True
            
            usercourse = UserCourse(user=payment.user, course=payment.course)
            usercourse.save()
            payment.user_course = usercourse
            payment.save()
            return render(request, 'courses/my_courses.html')
        except:
            return HttpResponse('payment failed')
        