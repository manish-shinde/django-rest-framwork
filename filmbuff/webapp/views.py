from django.shortcuts import render
from django.http import HttpResponse #to get response
from django.shortcuts import get_object_or_404   #for handling 404 error
from rest_framework.views import APIView   #for returning Api data in normal view
from rest_framework.response import Response #handles http responses
from rest_framework import status #handles status
from .models import Movies
from .serializers import MovieSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
class MovieList(APIView):
    def get(self,request):
        movies1 = Movies.objects.all()
        serializer = MovieSerializer(movies1,many=True)
        # not working
        # filter_backends = (DjangoFilterBackend)
        # filter_fields = ('year','name','director')
        return Response(serializer.data)

    def post(self):
        pass
