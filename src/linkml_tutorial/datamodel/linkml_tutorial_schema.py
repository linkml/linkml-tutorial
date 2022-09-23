# Auto generated from linkml_tutorial.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-09-23T09:47:31
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
from linkml_runtime.linkml_model.types import Date, Integer, String
from linkml_runtime.utils.metamodelcore import XSDDate

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
linkml_tutorial = CurieNamespace('linkml_tutorial', 'https://w3id.org/linkml/linkml-tutorial/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = linkml_tutorial


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

    class_class_uri: ClassVar[URIRef] = linkml_tutorial.NamedThing
    class_class_curie: ClassVar[str] = "linkml_tutorial:NamedThing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = linkml_tutorial.NamedThing

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

    class_class_uri: ClassVar[URIRef] = linkml_tutorial.Person
    class_class_curie: ClassVar[str] = "linkml_tutorial:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = linkml_tutorial.Person

    id: Union[str, PersonId] = None
    vital_status: str = None
    primary_email: Optional[str] = None
    pets: Optional[Union[Union[str, AnimalId], List[Union[str, AnimalId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        if self._is_empty(self.vital_status):
            self.MissingRequiredField("vital_status")
        if not isinstance(self.vital_status, str):
            self.vital_status = str(self.vital_status)

        if self.primary_email is not None and not isinstance(self.primary_email, str):
            self.primary_email = str(self.primary_email)

        if not isinstance(self.pets, list):
            self.pets = [self.pets] if self.pets is not None else []
        self.pets = [v if isinstance(v, AnimalId) else AnimalId(v) for v in self.pets]

        super().__post_init__(**kwargs)


@dataclass
class Animal(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = linkml_tutorial.Animal
    class_class_curie: ClassVar[str] = "linkml_tutorial:Animal"
    class_name: ClassVar[str] = "Animal"
    class_model_uri: ClassVar[URIRef] = linkml_tutorial.Animal

    id: Union[str, AnimalId] = None
    species: Optional[str] = None
    breed: Optional[str] = None
    color: Optional[str] = None
    weight_in_mgs: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnimalId):
            self.id = AnimalId(self.id)

        if self.species is not None and not isinstance(self.species, str):
            self.species = str(self.species)

        if self.breed is not None and not isinstance(self.breed, str):
            self.breed = str(self.breed)

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

    class_class_uri: ClassVar[URIRef] = linkml_tutorial.PersonCollection
    class_class_curie: ClassVar[str] = "linkml_tutorial:PersonCollection"
    class_name: ClassVar[str] = "Person_Collection"
    class_model_uri: ClassVar[URIRef] = linkml_tutorial.PersonCollection

    entries: Optional[Union[Dict[Union[str, PersonId], Union[dict, Person]], List[Union[dict, Person]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="entries", slot_type=Person, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=linkml_tutorial.id, name="id", curie=linkml_tutorial.curie('id'),
                   model_uri=linkml_tutorial.id, domain=None, range=URIRef)

slots.name = Slot(uri=linkml_tutorial.name, name="name", curie=linkml_tutorial.curie('name'),
                   model_uri=linkml_tutorial.name, domain=None, range=Optional[str])

slots.primary_email = Slot(uri=linkml_tutorial.primary_email, name="primary_email", curie=linkml_tutorial.curie('primary_email'),
                   model_uri=linkml_tutorial.primary_email, domain=None, range=Optional[str])

slots.birth_date = Slot(uri=linkml_tutorial.birth_date, name="birth date", curie=linkml_tutorial.curie('birth_date'),
                   model_uri=linkml_tutorial.birth_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.age_in_years = Slot(uri=linkml_tutorial.age_in_years, name="age_in_years", curie=linkml_tutorial.curie('age_in_years'),
                   model_uri=linkml_tutorial.age_in_years, domain=None, range=Optional[int])

slots.vital_status = Slot(uri=linkml_tutorial.vital_status, name="vital_status", curie=linkml_tutorial.curie('vital_status'),
                   model_uri=linkml_tutorial.vital_status, domain=None, range=str)

slots.pets = Slot(uri=linkml_tutorial.pets, name="pets", curie=linkml_tutorial.curie('pets'),
                   model_uri=linkml_tutorial.pets, domain=None, range=Optional[Union[Union[str, AnimalId], List[Union[str, AnimalId]]]])

slots.household_members = Slot(uri=linkml_tutorial.household_members, name="household_members", curie=linkml_tutorial.curie('household_members'),
                   model_uri=linkml_tutorial.household_members, domain=None, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.species = Slot(uri=linkml_tutorial.species, name="species", curie=linkml_tutorial.curie('species'),
                   model_uri=linkml_tutorial.species, domain=None, range=Optional[str])

slots.breed = Slot(uri=linkml_tutorial.breed, name="breed", curie=linkml_tutorial.curie('breed'),
                   model_uri=linkml_tutorial.breed, domain=None, range=Optional[str])

slots.color = Slot(uri=linkml_tutorial.color, name="color", curie=linkml_tutorial.curie('color'),
                   model_uri=linkml_tutorial.color, domain=None, range=Optional[str])

slots.weight_in_mgs = Slot(uri=linkml_tutorial.weight_in_mgs, name="weight_in_mgs", curie=linkml_tutorial.curie('weight_in_mgs'),
                   model_uri=linkml_tutorial.weight_in_mgs, domain=None, range=Optional[str])

slots.entries = Slot(uri=linkml_tutorial.entries, name="entries", curie=linkml_tutorial.curie('entries'),
                   model_uri=linkml_tutorial.entries, domain=None, range=Optional[Union[Dict[Union[str, PersonId], Union[dict, Person]], List[Union[dict, Person]]]])