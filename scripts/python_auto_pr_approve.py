import os
from github3 import login
import json

# Get the Github token from the environment variable
github_token = os.getenv('GH_TOKEN')

# List of files to trigger auto-approval
files_to_trigger_approval = ['README.md', 'build_and_push.py']

# Login to Github using the token
gh = login(token=github_token)

# Get the pull request event payload from the environment variable
event_payload = os.getenv('GITHUB_EVENT_PATH')

# Load the payload
with open(event_payload, 'r') as f:
    payload = f.read()

# Parse the payload
payload_data = json.loads(payload)

# Get the pull request number and repository
pr_number = payload_data['number']
repo_name = payload_data['repository']['full_name']

# Get the repository object
repo = gh.repository(repo_name)

# Get the pull request object
pr = repo.pull_request(pr_number)

# Get the list of files changed in the pull request
files_changed = [file['filename'] for file in pr.files()]

# Check if any of the files to trigger auto-approval are changed
if any(file in files_changed for file in files_to_trigger_approval):
    # Add the reviewer (you can add more reviewers if needed)
    pr.add_reviewer('Python Auto Approval')

    # Approve the pull request
    pr.create_review(commit_id=pr.head.sha, event='APPROVE')