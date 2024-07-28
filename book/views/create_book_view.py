from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from book.serializers import BookSerializer
from book.services.book_service import BookService


class BookView(APIView):

    def get(self, request):
        """Handle GET requests to retrieve a list of all books"""
        try:
            books_list = BookService.get_list_book()
            serializer = BookSerializer(books_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": e})

    def post(self, request):
        """
        Handle POST requests to create a new book.
        Example: {
            "title": str,
            "author": str,
            "pages": int,
            "description": str,
            "published_date": date
        }
        """
        try:
            serializer = BookSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except (ValueError, TypeError) as e:
            return Response({"error": e}, status=status.HTTP_400_BAD_REQUEST)
