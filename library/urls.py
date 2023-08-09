from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('book-list/', views.BookListView.as_view(), name='book_list'),
    path('my-book-list/', views.MyBookListView.as_view(), name='my_book_list'),
    path('add/', views.BookCreateView.as_view(), name='book_add'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.CustomRegisterView.as_view(), name='register'),
    path('book/<int:book_id>/update/', views.update_book, name='book_update'),
    path('book/<int:book_id>/delete/', views.delete_book, name='book_delete'),
]
