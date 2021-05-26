#!/bin/zsh

export VERSION=""
export COMMENT=""

git add .
git commit -m $COMMENT
git push -u origin main

git tag -a $VERSION -m $COMMENT
git push origin $VERSION


# Build package
python3 setup.py sdist bdist_wheel

# Deploy package to PyPi
python3 -m twine upload --repository pypi dist/* --verbose

