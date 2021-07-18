from stix2 import ExtensionDefinition
from stix2 import CustomObject, properties
from stix2 import Incident
from stix2 import MarkingDefinition, StatementMarking
from stix2 import FileSystemStore, FileSystemSource

from stix2.workbench import get, set_default_created, set_default_object_marking_refs, save, add_data_source, create

ID = "identity--ea338c32-7ee0-4c77-86fd-d6c2f05f51c2"

MARKING_DEFINITIONS = [
    "marking-definition--70d2126c-14cb-48cf-b21e-dd5191c054a4",
    "marking-definition--cfda9a3e-68de-499e-8733-c576b9cb3be2"
]

EXTENSION_TYPES = [
    'new-sdo',
    'new-sro',
    'new-sco',
    'toplevel-property-extension',
    'property-extension'
]


fstore = FileSystemStore('common', bundlify=True, allow_custom=True)
fsource = FileSystemSource('common')

add_data_source(fsource)

me = get(ID)


set_default_created("2021-07-06T02:48:10.667445Z")


m0 = MarkingDefinition(definition_type='statement',
                       created_by_ref=me,
                       id=MARKING_DEFINITIONS[0],
                       definition=StatementMarking('Copyright 2021, Civic Hacker, LLC.'))

m1 = MarkingDefinition(definition_type='statement',
                       created_by_ref=me,
                       id=MARKING_DEFINITIONS[1],
                       definition=StatementMarking('This content is subject to open source license terms expressed in the BSD-3-Clause License. For more information, please see https://github.com/civichacker/love-language'))

set_default_object_marking_refs([m0, m1])

c = create(
    ExtensionDefinition,
    name='Use of Force',
    created_by_ref=me,
    description='This schema creates a new object type called Use of Force',
    version=1.0,
    schema='https://raw.githubusercontent.com/civichacker/love-language/master/schemas/use-of-force.schema.json',
    extension_properties=[
        'x_civichacker_force_applied',
        'x_civichacker_deadly_force'
    ],
    extension_types=[
        'toplevel-property-extension',
        'property-extension',
        'new-sro'
    ])


print(c.serialize(pretty=True))


@CustomObject(
    'x-use-of-force', [
        ('name', properties.StringProperty(required=False)),
        ('identity_ref', properties.ReferenceProperty(valid_types=['identity'], required=True)),
        ('incident_ref', properties.ReferenceProperty(valid_types=['incident'], required=True)),
    ], extension_name=c.id, is_sdo=False,
)
class UseOfForce:
    pass


fake_incident = Incident(name='Something Bad happened')

uof = create(UseOfForce, identity_ref=me, incident_ref=fake_incident)

print(uof.serialize(pretty=True))


# fstore.add(c)
