"""Modified views 
    for the school app project
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact-us', views.contact_view, name='contact'),
    path('signup', views.signup_view, name='signup'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout_page'),
    path('debtors', views.current_debtors, name='current_debtors'),
    path('debtor_email', views.debtor_email, name='debtor-email'),
    path('about', views.about_us, name='about'),
    path('faq', views.faq, name='faq'),
    path('verification/', views.verify_otp, name='verify_otp'),
    path('verification-success/', views.verification_success, name='verification_success'),
    path('verification-fail/', views.verification_fail, name='verification_fail'),
    path('resend-code/', views.resend_otp, name='resend_otp'),
]