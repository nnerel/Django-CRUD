from django.urls import path

from . import views

app_name = 'books'

urlpatterns = [
    path('', views.BookList.as_view(), name='book_list'),
    path('<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
    path('add', views.BookCreate.as_view(), name='book_create'),
    path('edit/<int:pk>/', views.BookUpdate.as_view(), name='book_update'),
    path('delete/<int:pk>/', views.BookDelete.as_view(), name='book_delete'),

]
