import os
from github import Github
import pdb



# List of files to trigger auto-approval
files_to_trigger_approval = ['README.md', 'python_auto_pr_approve.py']


def trigger_approval(file, files_to_trigger_approval):
    # Get the Github token from the environment variable
    github_token = os.getenv('GH_TOKEN')

    if github_token == '':
        return "GITHUB_TOKEN environment variable is not set"

    # Login to Github using the token   
    try:   
        gh = Github(os.getenv('GH_TOKEN'))
  
        # Get the repository and pull request from the github context
        repository = gh.get_repo(os.getenv('GITHUB_REPOSITORY'))
        pull_request_number = int(os.getenv('PULL_REQUEST_NUMBER'))
        pull_request = repository.get_pull(int(pull_request_number))

        # Get more information

        print(f"Pull request: {pull_request.number} - {pull_request.title}")
        print(f"Repository: {repository.name}")
        print(f"Repository owner: {repository.owner.login}")
        print(f"Pull request state: {pull_request.state}")

        # Get the list of files changed in the pull request
        files_changed = [file.filename for file in pull_request.get_files()]

        # Check if any of the files to trigger auto-approval are changed
        if any(file in files_changed for file in files_to_trigger_approval):
            # Get the reviewer
                reviewer = 'natan-bot'
                try:
                    # Check if the reviewer is a valid GitHub user
                    gh.get_user(reviewer)
                    print(f"Reviewer is valid: {reviewer}")
                except Exception as e:
                    print(f"Error: {e}")
                    print("Reviewer is not a valid GitHub user")
                else:
                    # Add the reviewer
                    pull_request.create_review_request(reviewers=[reviewer])
                    # Approve the pull request
                    pull_request.create_review(body='Approved', event='APPROVE')
    except Exception as e:
        print(f"Error: {e}")
        return "invalid token"
#if __name__ == '__main__':
#    trigger_approval(file, files_to_trigger_approval)