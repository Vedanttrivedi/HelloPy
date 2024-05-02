#!/bin/bash

ids="/subscriptions/e1231fd8-853d-4f48-80b3-6fdc695638e7/resourcegroups/managed-identity-test/providers/Microsoft.Web/sites/python-app-identity"
echo $ids
repo_url=https://github.com/Vedanttrivedi/HelloPy
echo $repo_url
az webapp deployment source config --branch main --manual-integration  --repo-url $repo_url --ids $ids
az webapp deployment source sync --ids $ids --name $name
echo "pushing"
