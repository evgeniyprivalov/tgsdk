rm -rf htmlcov/

cd ../../

pytest --cov=tgsdk tests \
--cov-report html \
--cov-report term

#coverage report -m
