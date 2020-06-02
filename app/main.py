import os
import requests  # noqa We are just importing this to prove the dependency installed correctly


def main():
    workflow_file_name = os.environ.get("GITHUB_WORKFLOW", False)
    token = os.environ.get("GITHUB_TOKEN", False)
    repo = os.environ.get("GITHUB_REPOSITORY", False)
    print(workflow_file_name)
    if workflow_file_name and token:
        headers = {'Authorization': 'token ' + token}
        url = 'https://api.github.com/repos/{0}/actions/workflows'.format(repo)
        response = requests.get(url, headers=headers)
        if response != requests.codes.ok:
            return 1
        workflow_id = response.json().get('workflows')[0].get('id', False)
        print(f"::set-output name=WORKFLOW_ID::{workflow_id}")
    return 0


if __name__ == "__main__":
    exit(main())
