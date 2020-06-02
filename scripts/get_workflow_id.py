#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess
import sys
import shlex

import requests


def main(argv=None):
    if argv is None:
        argv = sys.argv
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
        strcmd_exe = 'echo "::set-output name=WORKFLOW_ID::{0}"'.format(
            workflow_id)
        cmd = shlex.split(strcmd_exe)
        try:
            proc = subprocess.Popen(
                cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdoutdata, stderrdata = proc.communicate()
            if proc.wait() != 0:
                return 1
        except Exception as e:
            print(e)
            return 1
    return 0


if __name__ == '__main__':
    exit(main())
