from democracywatcher.apps.tracker.models import Deputy, Ballot, Vote
from democracywatcher.apps.tracker.serializers import DeputySerializer, DeputyVotesSerializer, BallotSerializer, VoteSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics


class DeputyList(generics.ListAPIView):
    queryset = Deputy.objects.all()
    serializer_class = DeputySerializer
