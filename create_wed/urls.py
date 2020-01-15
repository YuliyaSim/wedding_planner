from django.urls import path
from create_wed import views
from create_wed.views import ContactUs

app_name = 'create_wed'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('create_wedding/', views.create_weeding_view, name='create_wedding'),
    path('contact/', ContactUs.as_view(), name='contact'),
    path('services/', views.services, name='services'),

]

