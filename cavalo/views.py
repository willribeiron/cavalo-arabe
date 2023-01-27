from django.shortcuts import render
from rest_framework import viewsets
from cavalo.serializers import CardSerializer
from cavalo.serializers import Card


class CardViewset(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all()

# Create your views here.
