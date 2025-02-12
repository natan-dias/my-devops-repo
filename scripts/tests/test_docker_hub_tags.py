import pytest
import requests
import json
from pytest_mock import mocker

# Small workaround to use absolute imports
import sys
from pathlib import Path # if you haven't already done so
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

# Additionally remove the current file's directory from sys.path
try:
    sys.path.remove(str(parent))
except ValueError: # Already removed
    pass

from docker_hub_tags import get_tags

class MockResponse:
    def __init__(self, status_code, json_data=None):
        self.status_code = status_code
        self.json_data = json_data

    def json(self):
        return self.json_data

def test_get_tags_success(mocker):
    # Mock the requests.get function to return a successful response
    mocker.patch('requests.get', return_value=MockResponse(200, {'results': [{'name': 'test', 'tag_status': 'active', 'tag_last_pushed': '2023-02-20T14:30:00.000Z'}]}))

    # Call the get_tags function
    tags = get_tags('test_repository', 'test_image')

    # Assert that the function returns the expected result
    assert len(tags) == 1
    assert tags[0]['name'] == 'test'
    assert tags[0]['status'] == 'active'
    assert tags[0]['last_pushed'] == '2023-02-20T14:30:00.000Z'

def test_get_tags_failure(mocker):
    # Mock the requests.get function to return a failed response
    mocker.patch('requests.get', return_value=MockResponse(404))

    # Call the get_tags function
    tags = get_tags('test_repository', 'test_image')

    # Assert that the function returns an empty list
    assert tags == []

def test_get_tags_invalid_repository():
    # Call the get_tags function with an invalid repository name
    with pytest.raises(TypeError):
        get_tags(None, 'test_image')

def test_get_tags_invalid_image():
    # Call the get_tags function with an invalid image name
    with pytest.raises(TypeError):
        get_tags('test_repository', None)