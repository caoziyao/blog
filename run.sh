
docker-compose down
docker-compose -f docker-compose.yml -f srv-pyapp.yml -f srv-greeter.yml  up --build