from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets
from .models import Language
from .serializers import LanguageSerializer

class LanguageView(viewsets.ModelViewSet): 
	queryset = Language.objects.all()
	serializer_class = LanguageSerializer