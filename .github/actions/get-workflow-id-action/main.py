import os
import requests  # noqa We are just importing this to prove the dependency installed correctly


def main():
    token = os.environ.get("INPUT_ACCESS_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY")
    if not token and repo:
        return 1
    headers = {'Authorization': 'token ' + token}
    url = f'https://api.github.com/repos/{repo}/actions/workflows/build.yml'
    r = requests.get(url, headers=headers)
    if r.status_code != requests.codes.ok:
        return 1
    workflow_id = r.json().get('id', False)
    print(f"::set-output name=workflow_id::{workflow_id}")
    return 0


if __name__ == "__main__":
    exit(main())
