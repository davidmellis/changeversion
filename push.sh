#!/usr/bin/bash

bumpfile="$1/.bumpversion.toml"

git config --global user.email "david.ellis@iongroup.com"
git config --global user.name "davidmellis"

git remote set-url origin git@github.com:davidmellis/testci.git


# https://github.com/davidmellis/testci.git

git config --list --show-origin 


pip install bumpversion
bumpversion --allow-dirty --commit --tag --config-file="$bumpfile" --new-version=0.0.$2 --list patch
git push origin HEAD:main
