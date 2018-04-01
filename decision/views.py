from .models import Decision, Point
from .serializers import DecisionSerializer, PointSerializer

from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly, AllowAny

from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend

class DecisionFilter(generics.ListCreateAPIView):
    queryset = Decision.objects.all().order_by('-popularity')
    serializer_class = DecisionSerializer
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_fields = ('is_published',)
    search_fields = ('name1', 'name2')
    pagination_class = PageNumberPagination


@api_view(['GET'])
def decision_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        decision = Decision.objects.get(pk=pk)
        decision.popularity +=1
        decision.save()
    except Decision.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DecisionSerializer(decision)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def points(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        points = Point.objects.filter(decision=pk)
    except Point.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PointSerializer(points, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PointSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)