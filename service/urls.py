from django.urls import path
from service import views

urlpatterns = [
    path('members/',views.func),
    path('members/details/<int:id>', views.details),
    path('',views.main),
]