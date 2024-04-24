#!/bin/bash

ids=$(az webapp list --query '[0].id' -o tsv)
echo $ids
name="HelloPy"
repo_url=https://github.com/Vedanttrivedi/HelloPy
echo $repo_url
az webapp deployment source config --branch main --manual-integration --name $name --repo-url $repo_url --ids $ids
az webapp deployment source sync --ids $ids --name $name
echo "pushing"
