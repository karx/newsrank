from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from pageranker.models import Vote
from rest_framework import viewsets
from pageranker.serializers import VoteSerializer
from rest_framework import generics

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



# class VoteViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Vote.objects.all()
#     serializer_class = VoteSerializer

class VoteList(generics.ListAPIView):
    # logger.debug ("My Vote List.")
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    
    # def get_queryset(self):
    #     resident = self.request.user.resident
    #     return resident.get_all_sp_visits()
