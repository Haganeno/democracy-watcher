import requests
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from democracywatcher.apps.tracker.schemas import Deputy, Ballot, Vote
from democracywatcher.apps.tracker.serializers import DeputySerializer, BallotSerializer, VoteUpdateSerializer
from democracywatcher.apps.tracker.models import Vote as VoteModel, Ballot as BallotModel


class ParliamentTracker:
    DEPUTIES_URL = 'https://www.nosdeputes.fr/deputes/enmandat/json'
    BALLOT_URL = 'https://www.nosdeputes.fr/16/scrutins/json'
    VOTE_URL = 'https://www.nosdeputes.fr/16/scrutin/%s/json'

    def __init__(self):
        self.deputies = None
        self.ballots = None
        self.votes = None
        self.slug_deputies = None
   
    def load_all_deputies(self):
        res = requests.get(self.DEPUTIES_URL)
        if res.status_code != 200:
            # warning
            return

        self.deputies = []
        self.slug_deputies = {}
        for item in res.json()['deputes']:
            deputy = Deputy(**item['depute'])
            self.deputies.append(deputy)
            self.slug_deputies[item['depute']['slug']] = deputy
    
    def dump_all_deputies(self):
        for deputy in self.deputies:
            serializer = DeputySerializer(data=deputy.dict())
            if serializer.is_valid():
                serializer.save()
    
    def load_all_ballots(self):
        res = requests.get(self.BALLOT_URL)
        if res.status_code != 200:
            # warning
            return

        self.ballots = []
        for item in res.json()['scrutins']:
            ballot = Ballot(**item['scrutin'])
            self.ballots.append(ballot)
    
    def dump_all_ballots(self):
        for ballot in self.ballots:
            serializer = BallotSerializer(data=ballot.dict())
            if serializer.is_valid():
                serializer.save()
    
    def load_all_votes(self, ballot_number):
        db_vote = VoteModel.objects.filter(ballot_id=int(ballot_number)).count()
        if db_vote > 0:
            return

        res = requests.get(self.VOTE_URL % ballot_number)
        if res.status_code != 200:
            # warning
            return

        for item in res.json()['votes']:
            vote = Vote(**item['vote'])
            vote.ballot = item['vote']['scrutin']['numero']
            try:
                vote.deputy = self.slug_deputies[item['vote']['parlementaire_slug']].id
            except KeyError:
                pass
            print(vote.ballot)
            self.votes.append(vote)

    def dump_all_votes(self):
        for vote in self.votes:
            print(vote.ballot)
            serializer = VoteUpdateSerializer(data=vote.dict())
            if serializer.is_valid():
                serializer.save()
    
    def load_all_data(self):
        self.load_all_deputies()
        self.load_all_ballots()
        self.votes = []
        for ballot in self.ballots:
            self.load_all_votes(ballot.id)
    
    def dump_all_data(self):
        self.dump_all_deputies()
        self.dump_all_ballots()
        self.dump_all_votes()
    


def run():
    tracker = ParliamentTracker()
    tracker.load_all_data()
    tracker.dump_all_data()