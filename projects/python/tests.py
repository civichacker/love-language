import importlib


def test_use_of_force_import():
    lib = importlib.import_module('lovelanguage')
    assert hasattr(lib, 'USEOFFORCE')
