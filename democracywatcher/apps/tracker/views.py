from democracywatcher.apps.tracker.models import Deputy, Ballot, Vote
from democracywatcher.apps.tracker.serializers import DeputySerializer, BallotSerializer, VoteSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics


class DeputyListView(generics.ListAPIView):
    queryset = Deputy.objects.all()
    serializer_class = DeputySerializer


class DeputyDetailView(generics.RetrieveAPIView):
    queryset = Deputy.objects.all()
    serializer_class = DeputySerializer


class BallotListView(generics.ListAPIView):
    queryset = Ballot.objects.all()
    serializer_class = BallotSerializer


class BallotDetailView(generics.RetrieveAPIView):
    queryset = Ballot.objects.all()
    serializer_class = DeputySerializer


class VoteListView(generics.ListAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

    def get_queryset(self):
        ballot_id = self.kwargs.get('ballot_id')
        if ballot_id:
            return Vote.objects.filter(ballot=ballot_id).order_by('id')

        deputy_id = self.kwargs.get('deputy_id')
        if deputy_id:
            return Vote.objects.filter(deputy=deputy_id).order_by('id')
        return Vote.objects.all().order_by('id')


class VoteDetailView(generics.RetrieveAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


