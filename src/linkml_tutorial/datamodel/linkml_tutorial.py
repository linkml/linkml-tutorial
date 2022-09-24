# Auto generated from linkml_tutorial.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-09-23T17:04:09
# Schema: linkml-tutorial
#
# id: https://w3id.org/linkml/linkml-tutorial
# description: A repostitory that walks through schema generation.
# license: MIT

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Date, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
FOODON = CurieNamespace('FOODON', 'http://example.org/UNKNOWN/FOODON/')
NCIT = CurieNamespace('NCIT', 'http://example.org/UNKNOWN/NCIT/')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
WIKIDATA = CurieNamespace('WIKIDATA', 'http://example.org/UNKNOWN/WIKIDATA/')
BIOLINK = CurieNamespace('biolink', 'http://example.org/UNKNOWN/biolink/')
FOAF = CurieNamespace('foaf', 'http://example.org/UNKNOWN/foaf/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
LINKML_TUTORIAL = CurieNamespace('linkml_tutorial', 'https://w3id.org/linkml/linkml-tutorial/')
ORCID = CurieNamespace('orcid', 'http://example.org/UNKNOWN/orcid/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = LINKML_TUTORIAL


# Types

# Class references
class NamedThingId(extended_str):
    pass


class PersonId(NamedThingId):
    pass


class AnimalId(NamedThingId):
    pass


@dataclass
class NamedThing(YAMLRoot):
    """
    The most generic type of entity that has a name
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Thing
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = LINKML_TUTORIAL.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    birth_date: Optional[Union[str, XSDDate]] = None
    age_in_years: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.birth_date is not None and not isinstance(self.birth_date, XSDDate):
            self.birth_date = XSDDate(self.birth_date)

        if self.age_in_years is not None and not isinstance(self.age_in_years, int):
            self.age_in_years = int(self.age_in_years)

        super().__post_init__(**kwargs)


@dataclass
class Person(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Person
    class_class_curie: ClassVar[str] = "schema:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = LINKML_TUTORIAL.Person

    id: Union[str, PersonId] = None
    vital_status: Union[str, "PersonStatus"] = None
    primary_email: Optional[str] = None
    pets: Optional[Union[Union[str, AnimalId], List[Union[str, AnimalId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        if self._is_empty(self.vital_status):
            self.MissingRequiredField("vital_status")
        if not isinstance(self.vital_status, PersonStatus):
            self.vital_status = PersonStatus(self.vital_status)

        if self.primary_email is not None and not isinstance(self.primary_email, str):
            self.primary_email = str(self.primary_email)

        if not isinstance(self.pets, list):
            self.pets = [self.pets] if self.pets is not None else []
        self.pets = [v if isinstance(v, AnimalId) else AnimalId(v) for v in self.pets]

        super().__post_init__(**kwargs)


@dataclass
class Animal(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_TUTORIAL.Animal
    class_class_curie: ClassVar[str] = "linkml_tutorial:Animal"
    class_name: ClassVar[str] = "Animal"
    class_model_uri: ClassVar[URIRef] = LINKML_TUTORIAL.Animal

    id: Union[str, AnimalId] = None
    species: Optional[Union[str, URIorCURIE]] = None
    breed: Optional[Union[str, URIorCURIE]] = None
    color: Optional[str] = None
    weight_in_mgs: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnimalId):
            self.id = AnimalId(self.id)

        if self.species is not None and not isinstance(self.species, URIorCURIE):
            self.species = URIorCURIE(self.species)

        if self.breed is not None and not isinstance(self.breed, URIorCURIE):
            self.breed = URIorCURIE(self.breed)

        if self.color is not None and not isinstance(self.color, str):
            self.color = str(self.color)

        if self.weight_in_mgs is not None and not isinstance(self.weight_in_mgs, str):
            self.weight_in_mgs = str(self.weight_in_mgs)

        super().__post_init__(**kwargs)


@dataclass
class PersonCollection(YAMLRoot):
    """
    A collection of things
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_TUTORIAL.PersonCollection
    class_class_curie: ClassVar[str] = "linkml_tutorial:PersonCollection"
    class_name: ClassVar[str] = "Person_Collection"
    class_model_uri: ClassVar[URIRef] = LINKML_TUTORIAL.PersonCollection

    entries: Optional[Union[Dict[Union[str, PersonId], Union[dict, Person]], List[Union[dict, Person]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="entries", slot_type=Person, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class AnimalCollection(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_TUTORIAL.AnimalCollection
    class_class_curie: ClassVar[str] = "linkml_tutorial:AnimalCollection"
    class_name: ClassVar[str] = "AnimalCollection"
    class_model_uri: ClassVar[URIRef] = LINKML_TUTORIAL.AnimalCollection

    animals: Optional[Union[Dict[Union[str, AnimalId], Union[dict, Animal]], List[Union[dict, Animal]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="animals", slot_type=Animal, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations
class PersonStatus(EnumDefinitionImpl):

    ALIVE = PermissibleValue(text="ALIVE",
                                 description="the person is living",
                                 meaning=PATO["0001421"])
    DEAD = PermissibleValue(text="DEAD",
                               description="the person is deceased",
                               meaning=PATO["0001422"])
    UNKNOWN = PermissibleValue(text="UNKNOWN",
                                     description="the vital status is not known")

    _defn = EnumDefinition(
        name="PersonStatus",
    )

class Breeds(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="Breeds",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=LINKML_TUTORIAL.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=LINKML_TUTORIAL.name, domain=None, range=Optional[str])

slots.primary_email = Slot(uri=SCHEMA.email, name="primary_email", curie=SCHEMA.curie('email'),
                   model_uri=LINKML_TUTORIAL.primary_email, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\S+@[\S+\.]+\S+'))

slots.birth_date = Slot(uri=SCHEMA.birthDate, name="birth date", curie=SCHEMA.curie('birthDate'),
                   model_uri=LINKML_TUTORIAL.birth_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.age_in_years = Slot(uri=LINKML_TUTORIAL.age_in_years, name="age_in_years", curie=LINKML_TUTORIAL.curie('age_in_years'),
                   model_uri=LINKML_TUTORIAL.age_in_years, domain=None, range=Optional[int])

slots.vital_status = Slot(uri=LINKML_TUTORIAL.vital_status, name="vital_status", curie=LINKML_TUTORIAL.curie('vital_status'),
                   model_uri=LINKML_TUTORIAL.vital_status, domain=None, range=Union[str, "PersonStatus"])

slots.pets = Slot(uri=LINKML_TUTORIAL.pets, name="pets", curie=LINKML_TUTORIAL.curie('pets'),
                   model_uri=LINKML_TUTORIAL.pets, domain=None, range=Optional[Union[Union[str, AnimalId], List[Union[str, AnimalId]]]])

slots.species = Slot(uri=LINKML_TUTORIAL.species, name="species", curie=LINKML_TUTORIAL.curie('species'),
                   model_uri=LINKML_TUTORIAL.species, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.breed = Slot(uri=LINKML_TUTORIAL.breed, name="breed", curie=LINKML_TUTORIAL.curie('breed'),
                   model_uri=LINKML_TUTORIAL.breed, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.color = Slot(uri=LINKML_TUTORIAL.color, name="color", curie=LINKML_TUTORIAL.curie('color'),
                   model_uri=LINKML_TUTORIAL.color, domain=None, range=Optional[str])

slots.weight_in_mgs = Slot(uri=LINKML_TUTORIAL.weight_in_mgs, name="weight_in_mgs", curie=LINKML_TUTORIAL.curie('weight_in_mgs'),
                   model_uri=LINKML_TUTORIAL.weight_in_mgs, domain=None, range=Optional[str])

slots.entries = Slot(uri=LINKML_TUTORIAL.entries, name="entries", curie=LINKML_TUTORIAL.curie('entries'),
                   model_uri=LINKML_TUTORIAL.entries, domain=None, range=Optional[Union[Dict[Union[str, PersonId], Union[dict, Person]], List[Union[dict, Person]]]])

slots.animals = Slot(uri=LINKML_TUTORIAL.animals, name="animals", curie=LINKML_TUTORIAL.curie('animals'),
                   model_uri=LINKML_TUTORIAL.animals, domain=None, range=Optional[Union[Dict[Union[str, AnimalId], Union[dict, Animal]], List[Union[dict, Animal]]]])

slots.Person_id = Slot(uri=SCHEMA.identifier, name="Person_id", curie=SCHEMA.curie('identifier'),
                   model_uri=LINKML_TUTORIAL.Person_id, domain=Person, range=Union[str, PersonId])