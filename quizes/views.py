from rest_framework import viewsets, pagination, filters
from .models import Quiz
from .serializers import QuizSerializer

# class QuizPagination(pagination.PageNumberPagination):
#     page_size = 1
#     page_size_query_param = 'page_size'
#     max_page_size = 100


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['topic__category', 'name']  
    filterset_fields = ['topic__category', 'name'] 
    # pagination_class = QuizPagination
    