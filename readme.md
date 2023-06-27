# Repository with openBIS Bugs

## What is this repository

This repository collects a series of openBIS bugs, one per branch.
The branches are named after the Jira ticket where the bug was reported.

## How to test bugs

1. Install docker
1. Install [taskfile](https://taskfile.dev/)
1. Checkout the branch corresponding to your bug
1. Run: `task run_test`
1. Check the output of the python docker container

## How to add new bugs

1. Create a branch. Ideally the name of the branch corresponds to the ticket id of the bug you want to reproduce.
2. Edit the python script [here](./pybis/app/test.py)
3. If needed, change the version of pybis in [requirements.txt](/pybis/requirements.txt)
4. Run: `task run_test`


