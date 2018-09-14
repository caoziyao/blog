

docker rm -f prj-kuaibiji_srv-notebook_1
docker-compose -p prj-kuaibiji -f srv-notebook.yml -f notebook/debug.yml  up -d --build
