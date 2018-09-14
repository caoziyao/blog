

docker rm -f prj-kuaibiji_srv-user_1
docker-compose -p prj-kuaibiji -f srv-user.yml -f user/produ.yml  up -d  --build
