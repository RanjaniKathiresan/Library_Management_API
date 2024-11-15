from django.urls import path
from .views import RegisterUser,AddBooks, logout_view

urlpatterns = [
   path('register/', RegisterUser.as_view(), name='register'),
   path('add_book/', AddBooks.as_view(), name='add_book'),
   path('logout/', logout_view, name='logout'),
]