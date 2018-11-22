#!/bin/bash

# only need to run this once for each repo

pip install yapf

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

curl https://raw.githubusercontent.com/google/yapf/master/plugins/pre-commit.sh -o pre-commit.sh && mv pre-commit.sh .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit
