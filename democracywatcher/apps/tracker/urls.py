from django.urls import path

from democracywatcher.apps.tracker.views import (
    DeputyListView, DeputyDetailView, BallotListView, BallotDetailView,
    VoteListView, VoteDetailView,
)


urlpatterns = [
    path('deputies/', DeputyListView.as_view(), name='deputy_list'),
    path('deputies/<str:pk>/', DeputyDetailView.as_view(), name='deputy_detail'),
    path('deputies/<str:deputy_id>/votes/', VoteListView.as_view(), name='vote_deputy_list'),
    path('ballots/', BallotListView.as_view(), name='ballot_list'),
    path('ballots/<str:pk>/', BallotDetailView.as_view(), name='ballot_detail'),
    path('ballots/<str:ballot_id>/votes/', VoteListView.as_view(), name='vote_ballot_list'),
    path('votes/<str:pk>/', VoteDetailView.as_view(), name='vote_detail'),
]
