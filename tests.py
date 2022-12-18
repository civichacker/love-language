from pathlib import Path
import json

import pytest

from jsonschema import Draft7Validator, validators
import jsonschema
from stix2validator import validate_file, print_results, ValidationOptions

EXTENSION_DIRECTORY = 'stix-extensions'
SCHEMA_DIRECTORY = 'schemas'


@pytest.mark.parametrize("example", [f.name for f in Path(EXTENSION_DIRECTORY).iterdir() if f.is_file()])
def test_stix_validation(example):
    options = ValidationOptions(strict=False, version="2.1", schema_dir=EXTENSION_DIRECTORY)
    results = validate_file(f"{EXTENSION_DIRECTORY}/{example}", options)
    print_results(results)
    assert results.is_valid

@pytest.mark.parametrize(
    "scenario",
    [
        {
            'example': 'deadly-force',
            'schema': 'use-of-force'
        }
    ])
def test_json_examples(scenario):
    i_path = f'./{EXTENSION_DIRECTORY}/{scenario["example"]}.json'
    s_path = f'./schemas/{scenario["schema"]}.schema.json'
    with open(i_path) as i, open(s_path) as s:
        schema = json.load(s)
        instance = json.load(i)
        v = jsonschema.validate(instance, schema)
    assert True


@pytest.mark.schemas
@pytest.mark.parametrize("schema_under_test", [f.name for f in Path(SCHEMA_DIRECTORY).iterdir() if f.is_file()])
def test_validate_in_house_schemas(schema_under_test):
    s_path = f'{SCHEMA_DIRECTORY}/{schema_under_test}'
    with open(s_path) as s:
        schema = json.load(s)
        assert validators.Draft202012Validator.check_schema(schema) is None
