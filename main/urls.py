from django.urls import path

from main.views import index, book_list, author_detail

urlpatterns = [
    path('', index, name='home'),
    path('<str:slug>/', book_list, name='book-list'),
    path('author/<int:pk>', author_detail, name='author-detail')
]















