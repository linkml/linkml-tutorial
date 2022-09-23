# Auto generated from linkml_tutorial.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-09-23T08:46:16
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



class Person(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = linkml_tutorial.Person
    class_class_curie: ClassVar[str] = "linkml_tutorial:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = linkml_tutorial.Person


# Enumerations


# Slots
class slots:
    pass

