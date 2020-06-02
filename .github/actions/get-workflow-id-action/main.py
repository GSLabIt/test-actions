import os
import requests  # noqa We are just importing this to prove the dependency installed correctly


def main():
    print('sticaz , access_token')
    token = os.environ.get("INPUT_ACCESS_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY")
    print('sticaz 2', token, repo, os.environ),
    if not token and repo:
        return 1
    headers = {'Authorization': 'token ' + token}
    url = f'https://api.github.com/repos/{repo}/actions/workflows/build.yml'
    response = requests.get(url, headers=headers)
    print(url, response.json())
    if response != requests.codes.ok:
        return 1
    workflow_id = response.json().get('workflows')[0].get('id', False)
    print('workflow_id', workflow_id)
    print(f"::set-output name=workflow_id::{workflow_id}")
    return 0


if __name__ == "__main__":
    exit(main())
