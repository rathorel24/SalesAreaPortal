from rest_framework import viewsets
from .models import RetailOutlets, DivOffice
from .seralization import RetailOutletsSerilizer, DivOfficeSerilizer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter



class RetailOutletModelViewset(viewsets.ModelViewSet):
    queryset = RetailOutlets.objects.all()
    serializer_class = RetailOutletsSerilizer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = '__all__'
    search_fields = ['code','name','area','sales','fieldofficer','type']
    ordering_fields = ['code','sales']

class DivOfficeModelViewset(viewsets.ModelViewSet):
    queryset = DivOffice.objects.all()
    serializer_class = DivOfficeSerilizer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'
