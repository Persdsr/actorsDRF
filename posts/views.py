from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Actor, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import ActorSerializer


class ActorAPIListPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10000


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = (IsAdminOrReadOnly, IsOwnerOrReadOnly)
    #pagination_class = ActorAPIListPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content']
    ordering = ['title']

    @action(methods=['get'], detail=True)
    def category(self, request, pk):
        category = Category.objects.get(pk=pk)
        return Response({'category': category.name})

