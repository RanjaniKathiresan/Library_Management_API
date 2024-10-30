from django.urls import path
from .views import RegisterUser,AddBooks

urlpatterns = [
   path('register/', RegisterUser.as_view(), name='register'),
   path('add_book/', AddBooks.as_view(), name='add_book'),
]