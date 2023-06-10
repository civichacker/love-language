from importlib.resources import files

USEOFFORCE = files('lovelanguage.schemas').joinpath('use-of-force.schema.json').read_text()

__all__ = ['USEOFFORCE']
