docker-compose down
docker-compose -f docker-compose.yml \
        -f  srv-pyapp.yml \
        -f srv-greeter.yml \
        -f srv-notebook.yml \
        -f srv-user.yml \
        -f produ.yml \
        up -d --build