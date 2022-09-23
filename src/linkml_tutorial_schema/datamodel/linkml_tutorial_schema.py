# Auto generated from linkml_tutorial_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-09-23T09:36:25
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
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
LINKML_TUTORIAL_SCHEMA = CurieNamespace('linkml_tutorial_schema', 'https://w3id.org/linkml/linkml-tutorial-schema/')
DEFAULT_ = LINKML_TUTORIAL_SCHEMA


# Types

# Class references



@dataclass
class Person(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_TUTORIAL_SCHEMA.Person
    class_class_curie: ClassVar[str] = "linkml_tutorial_schema:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = LINKML_TUTORIAL_SCHEMA.Person

    id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=LINKML_TUTORIAL_SCHEMA.id, name="id", curie=LINKML_TUTORIAL_SCHEMA.curie('id'),
                   model_uri=LINKML_TUTORIAL_SCHEMA.id, domain=None, range=Optional[str])