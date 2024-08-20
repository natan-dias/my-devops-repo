# tests/test_python_auto_pr_approve.py
import pytest
import os
from unittest.mock import patch, Mock
from github import Github

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

import python_auto_pr_approve

def test_trigger_approval():
    # Mock the Github token and the files to trigger approval
    github_token = 'mock_token'
    files_to_trigger_approval = ['README.md', 'python_auto_pr_approve.py']

    # Set the environment variables
    os.environ['GH_TOKEN'] = github_token
    os.environ['GITHUB_REPOSITORY'] = 'natan-dias/my-devops-repo'
    os.environ['PULL_REQUEST_NUMBER'] = '1'

    # Patch the Github Class
    with patch('python_auto_pr_approve.Github') as mock_gh:
        print(mock_gh)
        # Create a mocked Github object
        gh = mock_gh.return_value
        gh.get_repo.return_value = Mock()

        # Call the trigger_approval function
        try:
            python_auto_pr_approve.trigger_approval('README.md', files_to_trigger_approval)
        except Exception as e:
            print(f"An error occurred: {e}")
        
        # Print out the calls made to the mocked Github object
        print("Calls made to Github object:")
        for call in mock_gh.mock_calls:
            print(call)

        # Assert that the get_repo method was called
        gh.get_repo.assert_called_once_with(os.environ['GITHUB_REPOSITORY'])

def test_trigger_approval_no_token():
    # Set the environment variables
    os.environ['GH_TOKEN'] = ''
    os.environ['GITHUB_REPOSITORY'] = 'natan-dias/my-devops-repo'
    os.environ['PULL_REQUEST_NUMBER'] = '1'

    # Patch the Github class
    with patch('python_auto_pr_approve.Github') as mock_gh:
        # Call the trigger_approval function
        result = python_auto_pr_approve.trigger_approval('README.md', ['README.md'])

        # Assert that the result is an error message
        assert result == "GITHUB_TOKEN environment variable is not set"

def test_trigger_approval_invalid_token():
    # Set the environment variables
    os.environ['GH_TOKEN'] = 'invalid_token'
    os.environ['GITHUB_REPOSITORY'] = 'natan-dias/my-devops-repo'
    os.environ['PULL_REQUEST_NUMBER'] = '1'

    # Patch the Github class
    with patch('python_auto_pr_approve.Github') as mock_gh:
        # Create a mocked Github object
        gh = mock_gh.return_value
        gh.get_repo.side_effect = Exception("invalid token")

        # Call the trigger_approval function
        result = python_auto_pr_approve.trigger_approval('README.md', ['README.md'])

        # Assert that the result is an error message
        assert result == "invalid token"