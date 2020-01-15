from django.urls import path
from todo import views

app_name = 'todo'
urlpatterns = [
    path('todo_list/', views.index, name='todo_list'),
    path('create_coordination/', views.CreateCoordinationView.as_view(), name='create_coordination'),
    path('update_coordination/', views.UpdateCoordinationView.as_view(), name='update_coordination'),
    path('create_wedding_day/', views.CreateWeddingDayView.as_view(), name='create_wedding_day'),
    path('wedding_day/', views.WeddingDayView.as_view(), name='wedding_day'),
    ]
