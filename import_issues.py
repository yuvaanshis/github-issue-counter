#!/usr/bin/env python

import github3
from github3 import login
import pandas as pd

GITHUB_TOKEN = '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'
ORG = 'yuvaanshis'
REPO = 'new_batch'

FILENAME_ISSUES = ORG + 'issues.json'

gh = login( token=GITHUB_TOKEN )

issues = []
for i, issue in enumerate(gh.issues_on(ORG, REPO, state='all')):
    issues.append({'closed': issue.is_closed(), 'created': issue.created_at})
    print(f'got {i} issues...')

df = pd.DataFrame(issues)
with open(FILENAME_ISSUES, 'w') as f:
    f.write(df.to_json())
