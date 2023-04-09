from django.db import models

class Deputy(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.CharField(unique=True)
    first_name = models.CharField()
    surname = models.CharField()
    gender = models.CharField(blank=True, null=True)
    birthdate = models.DateField()
    birthplace = models.CharField()
    department_number = models.CharField()
    district = models.CharField()
    district_number = models.CharField()
    mandate_start_date = models.DateField()
    party_name = models.CharField()
    party_acronym = models.CharField()
    websites = models.JSONField()
    email_addresses = models.JSONField()
    addresses = models.JSONField()
    associates = models.JSONField()
    previous_mandates = models.JSONField()
    profession = models.CharField()
    twitter_name = models.CharField()
    url_an = models.CharField()
    id_an = models.CharField()

    class Meta:
        indexes = [
            models.Index(fields=['slug', 'slug'])
        ]
        ordering = ['surname']


class Ballot(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date = models.DateField()
    type = models.CharField()
    status = models.CharField()
    title = models.CharField()
    number_of_voters = models.CharField()
    for_votes = models.CharField()
    against_votes = models.CharField()
    abstention_votes = models.CharField()
    applicants = models.JSONField()
    an_url = models.CharField()


class Vote(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deputy_party_acronym = models.CharField(blank=True, null=True)
    vote = models.CharField()
    party_vote = models.CharField()
    delegated = models.BooleanField(default=True)

    ballot = models.ForeignKey(Ballot, on_delete=models.CASCADE)
    deputy = models.ForeignKey(Deputy, on_delete=models.CASCADE)
