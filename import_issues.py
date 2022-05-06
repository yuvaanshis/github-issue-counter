#!/usr/bin/env python
#import requests
import github3, json, os.path
import pandas as pd

from json_helpers import DateTimeEncoder

ORG = 'yuvaanshis'
REPO = 'new_batch'
GITHUB_TOKEN = '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'
FILENAME_ISSUES = ORG + 'issues.json'

#gh = Github(GITHUB_TOKEN)
#gh = Github()
#gh = github3.login(token=GITHUB_TOKEN)
#gh = Github("GITHUB_TOKEN")
gh = github3.login(token=GITHUB_TOKEN)

issues = []
for i, issue in enumerate(gh.issues_on(ORG, REPO, state='all')):
    issues.append({'closed': issue.is_closed(), 'created': issue.created_at})
    print(f'got {i} issues...')
	
df = pd.DataFrame(issues)
with open(FILENAME_ISSUES, 'w') as f:
    f.write(df.to_json())
