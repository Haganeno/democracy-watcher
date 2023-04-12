import json
import re
from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, Field


class MappingModel(BaseModel):
    class Config:
        allow_population_by_field_name = True
    
    def extract_date(self, key, data):
        mandates = []
        pattern = '(.*) / (.*) / (.*)'
        for item in data:
            groups = re.match(pattern, item[key]).groups()
            mandate = Mandate()
            if groups[0]:
                mandate.start_date=datetime.strptime(groups[0], '%d/%m/%Y')
            if groups[1]:
                mandate.end_date=datetime.strptime(groups[1], '%d/%m/%Y')
            mandates.append(json.loads(mandate.json()))
        return mandates


class Mandate(BaseModel):
    start_date: Optional[str]
    end_date: Optional[str]


class Deputy(MappingModel):
    def __init__(self, **kwargs):
        if 'sites_web' in kwargs:
            kwargs['websites'] = [item['site'] for item in kwargs['sites_web']]
        if 'emails' in kwargs:
            kwargs['email_addresses'] = [item['email'] for item in kwargs['emails']]
        if 'adresses' in kwargs:  
            kwargs['addresses'] = [item['adresse'] for item in kwargs['adresses']]
        if 'collaborateurs' in kwargs:  
            kwargs['associates'] = [item['collaborateur'] for item in kwargs['collaborateurs']]
        if 'anciens_mandats' in kwargs:
            kwargs['previous_mandates'] = self.extract_date('mandat', kwargs['anciens_mandats'])
        super().__init__(**kwargs)

    id: str = Field(None, alias="id")
    slug: str
    first_name: str = Field(None, alias="prenom")
    surname: str = Field(None, alias="nom_de_famille")
    gender: Optional[str] = Field(None, alias="sexe")
    birthdate: str = Field(None, alias="date_naissance")
    birthplace: str = Field(None, alias="lieu_naissance")
    department_number: str = Field(None, alias="num_deptmt")
    district: str = Field(None, alias="nom_circo")
    district_number: str = Field(None, alias="num_circo")
    mandate_start_date: date = Field(None, alias="mandat_debut")
    party_name: str = Field(None, alias="parti_ratt_financier")
    party_acronym: str = Field(None, alias="groupe_sigle")
    websites: Optional[list[str]]
    email_addresses: Optional[list[str]]
    addresses: Optional[list[str]]
    associates: Optional[list[str]]
    profession: str = Field(None, alias="profession")
    twitter_name: str = Field(None, alias="twitter")
    previous_mandates: Optional[list[Mandate]]
    seat_number: str = Field(None, alias="place_en_hemicycle")
    url_an: str
    id_an: str


class Vote(MappingModel):
    ballot: Optional[str]
    deputy: Optional[str]
    deputy_party_acronym: str = Field(None, alias='parlementaire_groupe_acronyme')
    deputy_slug: str = Field(None, alias='parlementaire_slug')
    vote: str = Field(None, alias='position')
    party_vote: str = Field(None, alias='position_groupe')
    delegated: bool = Field(None, alias='par_delegation')

    def __init__(self, **kwargs):
        if 'scrutin' in kwargs:
            kwargs['ballot'] = kwargs['scrutin']['numero']
        super().__init__(**kwargs)


class Ballot(MappingModel):
    id: str = Field(None, alias="numero")
    date: date
    type: str
    status: str = Field(None, alias="sort")
    title: str = Field(None, alias="titre")
    number_of_voters: str = Field(None, alias="nombre_votants")
    for_votes: int = Field(None, alias="nombre_pours")
    against_votes: int = Field(None, alias="nombre_contres")
    abstention_votes: str = Field(None, alias="nombre_abstentions")
    applicants: Optional[list[str]]
    an_url: str = Field(None, alias="url_institution")
    votes: Optional[list[Vote]]
