import importlib
import json


def test_use_of_force_import():
    lib = importlib.import_module('lovelanguage')
    assert hasattr(lib, 'USEOFFORCE')
    USEOFFORCE = getattr(lib, 'USEOFFORCE')
    force = json.loads(USEOFFORCE)
    assert 'force' in force.get('title')
