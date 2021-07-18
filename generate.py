from stix2 import Identity
from stix2 import CustomObject, properties
from stix2 import Bundle
from stix2 import MarkingDefinition, StatementMarking
from stix2 import FileSystemStore, MemoryStore


EXTENSION_TYPES = [
    'new-sdo',
    'new-sro',
    'new-sco',
    'toplevel-property-extension',
    'property-extension'
]

fs = FileSystemStore('extensions', bundlify=True, allow_custom=True)
ms = MemoryStore(allow_custom=True)

i = Identity(name="Civic Hacker, LLC",
             identity_class="organization")

m0 = MarkingDefinition(definition_type='statement',
                       created_by_ref=i,
                       definition=StatementMarking('Copyright 2021, Civic Hacker, LLC.'))

m1 = MarkingDefinition(definition_type='statement',
                       created_by_ref=i,
                       definition=StatementMarking('This content is subject to open source license terms expressed in the BSD-3-Clause License. For more information, please see https://github.com/civichacker/love-language'))


@CustomObject('extension-definition', [
    ('name', properties.StringProperty(required=True)),
    ('schema', properties.StringProperty(required=True)),
    ('version', properties.StringProperty(fixed='1.0')),
    ('extension_types', properties.ListProperty(properties.StringProperty)),
    ('description', properties.StringProperty()),
])
class ExtensionDefinition(object):
    def __init__(self, extension_types=None, **kwargs):
        if not isinstance(extension_types, list) or not all(map(lambda e: e in EXTENSION_TYPES, extension_types)):
            raise ValueError("'%s' is not a recognized class of animal." % extension_types)


c = ExtensionDefinition(name='Use of Force',
               created_by_ref=i,
               description='This schema creates a new object type called Use of Force',
               schema='https://raw.githubusercontent.com/civichacker/love-language/master/schemas/use-of-force.schema.json',
               object_marking_refs=[m0, m1],
               extension_types=['toplevel-property-extension', 'property-extension'])



print(c)

#fs.add([m0, m1])

fs.add([c])
ms.add([c])

ms.save_to_file(f'./extensions/{c.id}.json')
#fs.save_to_file(f'./extensions/s-{c.id}.json')


#print(bundle)
