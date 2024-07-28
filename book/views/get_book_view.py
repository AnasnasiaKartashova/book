from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from book.serializers import BookSerializer
from book.services.book_service import BookService


class GetOneBookView(APIView):

    def get(self, request, pk):
        """Get information about a book by its primary key (pk)"""
        try:
            book = BookService.get_info_book(pk)
            serializer = BookSerializer(book)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response(
                {"detail": "Book not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
