from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from pageranker.models import Vote
from rest_framework import viewsets
from pageranker.serializers import VoteSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



# class VoteViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Vote.objects.all()
#     serializer_class = VoteSerializer

class VoteList(generics.ListCreateAPIView):
    # logger.debug ("My Vote List.")
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    
    # def get_queryset(self):
    #     resident = self.request.user.resident
    #     return resident.get_all_sp_visits()

@api_view(['GET'])
def getVoteCounts(request):
    return Response(getUrlScore('abc'), status=status.HTTP_201_CREATED)
            

def getUrlScore(url):
    return "100"

  

# @api_view(['POST'])
# def newVoteReq(request):
#     try:
#         email = request.POST['email']
#         message = request.POST['message']
#         name = request.POST['name']
#         phone = request.POST['phone']
#         MsgService.sendSMS(['8437166272'],"New message from " + email + " (" + name + " : " + message)
#     except (KeyError, Choice.DataNotComplete):
#         logger.debug ("oops data not complete")
#         return Response("Nope",status=status.HTTP_201_CREATED)
#     else:
#         FrontpageMessage.objects.create(
#             email=email,
#             message=message,
#             name=name,
#             phone=phone,
#             submit_time=datetime.datetime.now()
#             )
#     return Response("TEST", status=status.HTTP_201_CREATED)
