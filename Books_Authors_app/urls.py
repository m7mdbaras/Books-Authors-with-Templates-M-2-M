from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('books/<int:book_id>', views.book_disply),
    path('add_book_author', views.add_book_author),
    path('add_book', views.add_book),

    path('authors', views.all_author),
    path('add_author', views.add_author),
    path('authors/<int:author_id>', views.show_author),
    path('add_author_book',views.add_author_book),
    
    

]
