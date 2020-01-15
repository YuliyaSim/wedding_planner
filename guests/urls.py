from django.urls import path

from guests import views
from guests.views import ManualGuestListView, UpdateManualGuestListView

app_name = 'guests'
urlpatterns = [
    # path('', views.index, name='index'),
    # path('guests-list/', GuestListView.as_view(), name='guests-list'),
    # path('party-list/', PartyListView.as_view(), name='party-list'),
    path('manual_guest_list/', ManualGuestListView.as_view(), name='manual_guest_list'),
    path('create_manual_guest_list/', UpdateManualGuestListView.as_view(), name='create_manual_guest_list'),
    path('send_email/', views.send_email, name='send_email'),

]
