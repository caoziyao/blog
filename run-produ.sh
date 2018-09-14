docker-compose -p prj-kuaibiji down --remove-orphans
docker-compose -p prj-kuaibiji  -f docker-compose.yml \
        -f srv-greeter.yml \
        -f produ.yml \
        up -d --build


cd services/py
sh notebook/run-srv-produ-notebook.sh
sh user/run-srv-produ-user.sh
sh weixin/run-srv-produ-weixin.sh
