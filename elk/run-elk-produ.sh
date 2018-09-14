
docker-compose -p prj-elk down
docker-compose -p prj-elk -f srv-elk.yml -f srv-elk-produ.yml up -d --build