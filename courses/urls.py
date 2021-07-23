
from django.urls import path
from .views import Home, CourseView, Signup, Login, signout, CheckoutView, PaymentSuccess
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', Home.as_view() , name='home' ),
    path('login', Login.as_view() , name='login' ),
    path('signup', Signup.as_view() , name='signup' ),
    path('logout', signout , name='logout' ),
    path('course/<str:slug>', CourseView.as_view() , name='course_page' ),
    path('checkout/<str:slug>', CheckoutView.as_view() , name='checkout_page' ),
    path('payment_success', PaymentSuccess.as_view() , name='payment' ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
