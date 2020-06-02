import os
import requests  # noqa We are just importing this to prove the dependency installed correctly


def main():
    print('sticaz')
    token = os.environ.get("INPUT_GITHUB_TOKEN", False)
    repo = os.environ.get("INPUT_GITHUB_REPOSITORY", False)
    print('sticaz 1', token, repo)
    if not token and repo:
        return 1
    headers = {'Authorization': 'token ' + token}
    url = f'https://api.github.com/repos/{repo}/actions/workflows/build.yml'
    response = requests.get(url, headers=headers)
    print(url, response.json())
    if response != requests.codes.ok:
        return 1
    workflow_id = response.json().get('workflows')[0].get('id', False)
    print(f"::set-output name=WORKFLOW_ID::{workflow_id}")
    return 0


if __name__ == "__main__":
    exit(main())
