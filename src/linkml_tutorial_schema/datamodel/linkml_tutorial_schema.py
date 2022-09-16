# Auto generated from linkml_tutorial_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-09-16T11:34:51
# Schema: linkml-tutorial-schema
#
# id: https://w3id.org/linkml/linkml-tutorial-schema
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
from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
LINKML_TUTORIAL_SCHEMA = CurieNamespace('linkml_tutorial_schema', 'https://w3id.org/linkml/linkml-tutorial-schema/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = LINKML_TUTORIAL_SCHEMA


# Types

# Class references



@dataclass
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_TUTORIAL_SCHEMA.NamedThing
    class_class_curie: ClassVar[str] = "linkml_tutorial_schema:NamedThing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = LINKML_TUTORIAL_SCHEMA.NamedThing

    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class Person(NamedThing):
    """
    Represents a Person:
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_TUTORIAL_SCHEMA.Person
    class_class_curie: ClassVar[str] = "linkml_tutorial_schema:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = LINKML_TUTORIAL_SCHEMA.Person

    primary_email: Optional[str] = None
    birth_date: Optional[str] = None
    age_in_years: Optional[str] = None
    vital_status: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.primary_email is not None and not isinstance(self.primary_email, str):
            self.primary_email = str(self.primary_email)

        if self.birth_date is not None and not isinstance(self.birth_date, str):
            self.birth_date = str(self.birth_date)

        if self.age_in_years is not None and not isinstance(self.age_in_years, str):
            self.age_in_years = str(self.age_in_years)

        if self.vital_status is not None and not isinstance(self.vital_status, str):
            self.vital_status = str(self.vital_status)

        super().__post_init__(**kwargs)


@dataclass
class PersonCollection(YAMLRoot):
    """
    A holder for Person objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_TUTORIAL_SCHEMA.PersonCollection
    class_class_curie: ClassVar[str] = "linkml_tutorial_schema:PersonCollection"
    class_name: ClassVar[str] = "PersonCollection"
    class_model_uri: ClassVar[URIRef] = LINKML_TUTORIAL_SCHEMA.PersonCollection

    entries: Optional[Union[Union[dict, Person], List[Union[dict, Person]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.entries, list):
            self.entries = [self.entries] if self.entries is not None else []
        self.entries = [v if isinstance(v, Person) else Person(**as_dict(v)) for v in self.entries]

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=LINKML_TUTORIAL_SCHEMA.id, name="id", curie=LINKML_TUTORIAL_SCHEMA.curie('id'),
                   model_uri=LINKML_TUTORIAL_SCHEMA.id, domain=None, range=Optional[str])

slots.name = Slot(uri=LINKML_TUTORIAL_SCHEMA.name, name="name", curie=LINKML_TUTORIAL_SCHEMA.curie('name'),
                   model_uri=LINKML_TUTORIAL_SCHEMA.name, domain=None, range=Optional[str])

slots.description = Slot(uri=LINKML_TUTORIAL_SCHEMA.description, name="description", curie=LINKML_TUTORIAL_SCHEMA.curie('description'),
                   model_uri=LINKML_TUTORIAL_SCHEMA.description, domain=None, range=Optional[str])

slots.primary_email = Slot(uri=LINKML_TUTORIAL_SCHEMA.primary_email, name="primary_email", curie=LINKML_TUTORIAL_SCHEMA.curie('primary_email'),
                   model_uri=LINKML_TUTORIAL_SCHEMA.primary_email, domain=None, range=Optional[str])

slots.birth_date = Slot(uri=LINKML_TUTORIAL_SCHEMA.birth_date, name="birth_date", curie=LINKML_TUTORIAL_SCHEMA.curie('birth_date'),
                   model_uri=LINKML_TUTORIAL_SCHEMA.birth_date, domain=None, range=Optional[str])

slots.age_in_years = Slot(uri=LINKML_TUTORIAL_SCHEMA.age_in_years, name="age_in_years", curie=LINKML_TUTORIAL_SCHEMA.curie('age_in_years'),
                   model_uri=LINKML_TUTORIAL_SCHEMA.age_in_years, domain=None, range=Optional[str])

slots.vital_status = Slot(uri=LINKML_TUTORIAL_SCHEMA.vital_status, name="vital_status", curie=LINKML_TUTORIAL_SCHEMA.curie('vital_status'),
                   model_uri=LINKML_TUTORIAL_SCHEMA.vital_status, domain=None, range=Optional[str])

slots.personCollection__entries = Slot(uri=LINKML_TUTORIAL_SCHEMA.entries, name="personCollection__entries", curie=LINKML_TUTORIAL_SCHEMA.curie('entries'),
                   model_uri=LINKML_TUTORIAL_SCHEMA.personCollection__entries, domain=None, range=Optional[Union[Union[dict, Person], List[Union[dict, Person]]]])