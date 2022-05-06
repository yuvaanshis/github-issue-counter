#!/usr/bin/env python
import requests
!pip install PyGithub
from github import Github
import json
import os.path
from prettytable import PrettyTable

from json_helpers import DateTimeEncoder

ORG = 'philips-software'
REPO = 'philips-software.github.io'
GITHUB_TOKEN = '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'
FILENAME_ISSUES = ORG + 'issues.json'

data = {}

if os.path.isfile(FILENAME_ISSUES):
	f = open(FILENAME_ISSUES)
	data = json.load(f)
	f.close()

gh = github.login(token=GITHUB_TOKEN)

if REPO not in data.keys():
	data[REPO] = {}

for i in gh.iter_repo_issues(ORG, REPO, state='all'):
	data[REPO][i.number] = {
		'created_at': i.created_at,
		'closed_at': i.closed_at,
		'is_pull_request': (i.pull_request is not None),
		'labels': [l.name for l in i.labels]
	}

f = open(FILENAME_ISSUES, 'w')
json.dump(data, f, cls=DateTimeEncoder)
f.close()
