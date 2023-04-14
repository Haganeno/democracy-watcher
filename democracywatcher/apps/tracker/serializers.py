from rest_framework import serializers
from democracywatcher.apps.tracker.models import Deputy, Vote, Ballot


class VoteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = [
            'id', 'created_at', 'updated_at', 'deputy_party_acronym', 'vote', 'party_vote',
            'delegated', 'ballot', 'deputy'
        ]


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = [
            'id', 'created_at', 'updated_at', 'deputy_party_acronym', 'vote', 'party_vote',
            'delegated', 'ballot', 'deputy'
        ]


class BallotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ballot
        fields = [
            'id', 'created_at', 'updated_at', 'date', 'type', 'status', 'title',
            'number_of_voters', 'for_votes', 'against_votes', 'abstention_votes',
            'applicants', 'an_url'
        ]


class DeputySerializer(serializers.ModelSerializer):
    class Meta:
        model = Deputy
        fields = [
            'id', 'created_at', 'updated_at', 'slug', 'first_name', 'surname',
            'gender', 'birthdate', 'birthplace', 'department_number', 'district',
            'district_number', 'mandate_start_date', 'party_name', 'party_acronym',
            'websites', 'email_addresses', 'addresses', 'associates', 'previous_mandates', 
            'profession', 'twitter_name', 'url_an', 'id_an'
        ]
