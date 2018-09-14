

docker rm -f prj-kuaibiji_srv-notebook_1
docker-compose -p prj-kuaibiji -f srv-notebook.yml -f notebook/produ.yml up -d --build