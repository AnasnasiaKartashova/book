from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from book.serializers import BookListFilterSerializer
from book.services.book_service import BookService


class GetListFilterView(APIView):
    """
    A view that retrieves a filtered list of books within a specified date range,
    and ranks them based on the number of pages in descending order.

    Args:
        - date_start (date): The start date for the filter range.
        - date_end (date): The end date for the filter range

    This corresponds to the SQL query:

    SELECT *,
    RANK() OVER(ORDER BY pages DESC) Rank
    FROM book
    WHERE published_date BETWEEN '2000-01-01' AND '2024-07-27';
    """

    def get(self, request):
        """ """
        data = request.query_params
        try:
            books_list = BookService.get_filter_list_book(data)
            serializer = BookListFilterSerializer(books_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": e})
