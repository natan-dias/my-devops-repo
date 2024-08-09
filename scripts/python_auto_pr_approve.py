import os
from github import Github

# Get the Github token from the environment variable
github_token = os.getenv('GH_TOKEN')

# List of files to trigger auto-approval
files_to_trigger_approval = ['README.md', 'file2.py']

# Login to Github using the token
gh = Github(github_token)

# Get the repository and pull request from the github context
repository = gh.get_repo(os.getenv('GITHUB_REPOSITORY'))
pull_request = os.getenv(int('PULL_REQUEST_NUMBER'))
#os.getenv('GITHUB_REF').split('/')[-1]
#if pull_request_number != 'merge':
#    pull_request = repository.get_pull(int(pull_request_number))
#else:
#    print("Pull request not found")

# Get the list of files changed in the pull request
files_changed = [file.filename for file in pull_request.get_files()]

# Check if any of the files to trigger auto-approval are changed
if any(file in files_changed for file in files_to_trigger_approval):
    # Add the reviewer (you can add more reviewers if needed)
    pull_request.create_review_request(reviewers=['Python Auto Approver'])

    # Approve the pull request
    pull_request.create_review(body='Approved', event='APPROVE')