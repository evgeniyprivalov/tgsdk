#!/bin/zsh

git add .
git commit -m "Update"
git push -u origin main


# Build package
python3 setup.py sdist bdist_wheel

# Deploy package to PyPi
python3 -m twine upload --repository pypi dist/* --verbose

