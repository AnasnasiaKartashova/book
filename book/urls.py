from django.urls import path
from book.views.create_book_view import BookView
from book.views.get_book_view import GetOneBookView
from book.views.get_list_filter_view import GetListFilterView


urlpatterns = [
    path("get_book/<int:pk>/", GetOneBookView.as_view(), name="get_book"),
    path("create_get_list_book/", BookView.as_view(), name="create_get_list_book"),
    path("get_book_filter/", GetListFilterView.as_view(), name="list_filter_book"),
]
