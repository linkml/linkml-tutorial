# Auto generated from linkml_tutorial.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-09-23T16:50:49
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
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
LINKML_TUTORIAL = CurieNamespace('linkml_tutorial', 'https://w3id.org/linkml/linkml-tutorial/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = LINKML_TUTORIAL


# Types

# Class references



@dataclass
class Person(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_TUTORIAL.Person
    class_class_curie: ClassVar[str] = "linkml_tutorial:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = LINKML_TUTORIAL.Person

    id: Union[str, URIorCURIE] = None
    vital_status: str = None
    name: Optional[str] = None
    primary_email: Optional[str] = None
    age_in_years: Optional[int] = None
    birth_date: Optional[Union[str, XSDDate]] = None
    pets: Optional[Union[Union[dict, "Animal"], List[Union[dict, "Animal"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, URIorCURIE):
            self.id = URIorCURIE(self.id)

        if self._is_empty(self.vital_status):
            self.MissingRequiredField("vital_status")
        if not isinstance(self.vital_status, str):
            self.vital_status = str(self.vital_status)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.primary_email is not None and not isinstance(self.primary_email, str):
            self.primary_email = str(self.primary_email)

        if self.age_in_years is not None and not isinstance(self.age_in_years, int):
            self.age_in_years = int(self.age_in_years)

        if self.birth_date is not None and not isinstance(self.birth_date, XSDDate):
            self.birth_date = XSDDate(self.birth_date)

        self._normalize_inlined_as_dict(slot_name="pets", slot_type=Animal, key_name="id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class Animal(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_TUTORIAL.Animal
    class_class_curie: ClassVar[str] = "linkml_tutorial:Animal"
    class_name: ClassVar[str] = "Animal"
    class_model_uri: ClassVar[URIRef] = LINKML_TUTORIAL.Animal

    id: Union[str, URIorCURIE] = None
    name: Optional[str] = None
    species: Optional[str] = None
    breed: Optional[str] = None
    color: Optional[str] = None
    weight_in_mgs: Optional[int] = None
    age_in_years: Optional[int] = None
    birth_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, URIorCURIE):
            self.id = URIorCURIE(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.species is not None and not isinstance(self.species, str):
            self.species = str(self.species)

        if self.breed is not None and not isinstance(self.breed, str):
            self.breed = str(self.breed)

        if self.color is not None and not isinstance(self.color, str):
            self.color = str(self.color)

        if self.weight_in_mgs is not None and not isinstance(self.weight_in_mgs, int):
            self.weight_in_mgs = int(self.weight_in_mgs)

        if self.age_in_years is not None and not isinstance(self.age_in_years, int):
            self.age_in_years = int(self.age_in_years)

        if self.birth_date is not None and not isinstance(self.birth_date, XSDDate):
            self.birth_date = XSDDate(self.birth_date)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=LINKML_TUTORIAL.id, name="id", curie=LINKML_TUTORIAL.curie('id'),
                   model_uri=LINKML_TUTORIAL.id, domain=None, range=Union[str, URIorCURIE])

slots.name = Slot(uri=LINKML_TUTORIAL.name, name="name", curie=LINKML_TUTORIAL.curie('name'),
                   model_uri=LINKML_TUTORIAL.name, domain=None, range=Optional[str])

slots.primary_email = Slot(uri=LINKML_TUTORIAL.primary_email, name="primary_email", curie=LINKML_TUTORIAL.curie('primary_email'),
                   model_uri=LINKML_TUTORIAL.primary_email, domain=None, range=Optional[str])

slots.birth_date = Slot(uri=LINKML_TUTORIAL.birth_date, name="birth date", curie=LINKML_TUTORIAL.curie('birth_date'),
                   model_uri=LINKML_TUTORIAL.birth_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.age_in_years = Slot(uri=LINKML_TUTORIAL.age_in_years, name="age_in_years", curie=LINKML_TUTORIAL.curie('age_in_years'),
                   model_uri=LINKML_TUTORIAL.age_in_years, domain=None, range=Optional[int])

slots.vital_status = Slot(uri=LINKML_TUTORIAL.vital_status, name="vital_status", curie=LINKML_TUTORIAL.curie('vital_status'),
                   model_uri=LINKML_TUTORIAL.vital_status, domain=None, range=str)

slots.pets = Slot(uri=LINKML_TUTORIAL.pets, name="pets", curie=LINKML_TUTORIAL.curie('pets'),
                   model_uri=LINKML_TUTORIAL.pets, domain=None, range=Optional[Union[Union[dict, Animal], List[Union[dict, Animal]]]])

slots.species = Slot(uri=LINKML_TUTORIAL.species, name="species", curie=LINKML_TUTORIAL.curie('species'),
                   model_uri=LINKML_TUTORIAL.species, domain=None, range=Optional[str])

slots.breed = Slot(uri=LINKML_TUTORIAL.breed, name="breed", curie=LINKML_TUTORIAL.curie('breed'),
                   model_uri=LINKML_TUTORIAL.breed, domain=None, range=Optional[str])

slots.color = Slot(uri=LINKML_TUTORIAL.color, name="color", curie=LINKML_TUTORIAL.curie('color'),
                   model_uri=LINKML_TUTORIAL.color, domain=None, range=Optional[str])

slots.weight_in_mgs = Slot(uri=LINKML_TUTORIAL.weight_in_mgs, name="weight_in_mgs", curie=LINKML_TUTORIAL.curie('weight_in_mgs'),
                   model_uri=LINKML_TUTORIAL.weight_in_mgs, domain=None, range=Optional[int])