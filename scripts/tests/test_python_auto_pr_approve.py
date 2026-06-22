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


def _setup_pr_mock(mock_gh, filenames):
    gh = mock_gh.return_value
    repo = Mock()
    pr = Mock()
    pr.number = 1
    pr.title = 'Test PR'
    pr.state = 'open'
    pr.get_files.return_value = [Mock(filename=f) for f in filenames]
    repo.get_pull.return_value = pr
    repo.name = 'my-devops-repo'
    repo.owner.login = 'natan-dias'
    gh.get_repo.return_value = repo
    return gh, pr


def test_trigger_approval_file_matches_valid_reviewer(capsys):
    os.environ['GH_TOKEN'] = 'mock_token'
    os.environ['GITHUB_REPOSITORY'] = 'natan-dias/my-devops-repo'
    os.environ['PULL_REQUEST_NUMBER'] = '1'

    with patch('python_auto_pr_approve.Github') as mock_gh:
        gh, pr = _setup_pr_mock(mock_gh, ['README.md'])
        gh.get_user.return_value = Mock()

        python_auto_pr_approve.trigger_approval('README.md', ['README.md'])

        pr.create_review_request.assert_called_once_with(reviewers=['natan-bot'])
        pr.create_review.assert_called_once_with(body='Approved', event='APPROVE')


def test_trigger_approval_file_matches_invalid_reviewer(capsys):
    os.environ['GH_TOKEN'] = 'mock_token'
    os.environ['GITHUB_REPOSITORY'] = 'natan-dias/my-devops-repo'
    os.environ['PULL_REQUEST_NUMBER'] = '1'

    with patch('python_auto_pr_approve.Github') as mock_gh:
        gh, pr = _setup_pr_mock(mock_gh, ['README.md'])
        gh.get_user.side_effect = Exception("User not found")

        python_auto_pr_approve.trigger_approval('README.md', ['README.md'])

        out = capsys.readouterr().out
        assert 'Reviewer is not a valid GitHub user' in out
        pr.create_review.assert_not_called()