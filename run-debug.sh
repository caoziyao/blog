
docker-compose -p prj-kuaibiji down --remove-orphans
docker-compose -p prj-kuaibiji -f docker-compose.yml \
        -f srv-greeter.yml \
        -f debug.yml \
        up -d --build

cd services/py
sh notebook/run-srv-debug-notebook.sh
sh user/run-srv-debug-user.sh
sh weixin/run-srv-debug-weixin.sh