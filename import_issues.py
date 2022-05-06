#!/usr/bin/env python
import requests
from github import Github
import json
import os.path

from json_helpers import DateTimeEncoder

ORG = 'philips-software'
REPO = 'philips-software.github.io'
# GITHUB_TOKEN = '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'
FILENAME_ISSUES = ORG + 'issues.json'


from github import Github

g = Github(base_url="https://github.com/api/v3", login_or_token="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")
r = g.get_repo("philips-software/philips-software.github.io")
for issue in r.get_issues(state='open'):
    for comment in issue.get_comments():
        print(comment)
data = {}

if os.path.isfile(FILENAME_ISSUES):
	f = open(FILENAME_ISSUES)
	data = json.load(f)
	f.close()

#gh = Github(GITHUB_TOKEN)
gh = Github(g)

if REPO not in data.keys():
	data[REPO] = {}

for i in gh.get_issues(ORG, REPO, state='all'):
	data[REPO][i.number] = {
		'created_at': i.created_at,
		'closed_at': i.closed_at,
		'is_pull_request': (i.pull_request is not None),
		'labels': [l.name for l in i.labels]
	}

f = open(FILENAME_ISSUES, 'w')
json.dump(data, f, cls=DateTimeEncoder)
f.close()
