rm -rf htmlcov/

set -a
. ../.env
set +a


cd ../../

pytest --cov=tgsdk tests \
--cov-report html \
--cov-report term

#coverage report -m
