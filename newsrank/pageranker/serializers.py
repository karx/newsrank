# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from pageranker.models import Vote


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ('vote','ip','url','host','vote_time','meta')

