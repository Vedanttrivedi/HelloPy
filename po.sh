#!/bin/bash
az login
ids=$(az webapp list --query '[0].id' -o tsv)
repo_url=https://github.com/Vedanttrivedi/HelloPy
az webapp deployment source config --branch main --manual-integration --repo-url $repo_url --ids $ids
az webapp deployment source sync --ids $ids