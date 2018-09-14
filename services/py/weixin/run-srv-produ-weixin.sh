

docker rm -f prj-kuaibiji_srv-weixin_1
docker-compose -p prj-kuaibiji -f srv-weixin.yml -f weixin/debug.yml  up -d  --build
