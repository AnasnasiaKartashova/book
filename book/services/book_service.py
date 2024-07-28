from django.db.models import Window, F
from django.db.models.functions import Rank
from book.models import Book


class BookService:

    @staticmethod
    def get_info_book(pk: int) -> Book:
        """Get information about a book by its primary key (pk)"""
        book = Book.objects.get(pk=pk)
        return book

    @staticmethod
    def get_list_book() -> list[Book]:
        """Get a list of all books"""
        books = Book.objects.all()
        return books

    @staticmethod
    def get_filter_list_book(data: dict) -> list[Book]:
        """
        Get a filtered list of books within a specified date range
        """
        date_start = data["date_start"]
        date_end = data["date_end"]
        books = Book.objects.filter(
            published_date__range=(date_start, date_end)
        ).annotate(rank=Window(expression=Rank(), order_by=F("pages").desc()))
        return books
