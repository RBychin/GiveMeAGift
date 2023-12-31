from django.urls import path

from .views import EventList, EventDetail, EventCreate, GiftCreate

app_name = 'event'

urlpatterns = [
    path('', EventList.as_view(), name='event_list'),
    path('<int:pk>/', EventDetail.as_view(), name='main'),
    path('create/', EventCreate.as_view(), name='event_create'),
    path('<int:pk>/create_gift/', GiftCreate.as_view(), name='gift_create')
]
