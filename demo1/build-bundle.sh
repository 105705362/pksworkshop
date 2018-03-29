docker build ./app -t harbor.pks.pcfdemo.com/demo/workshop-rest-server
docker push harbor.pks.pcfdemo.com/demo/workshop-rest-server
docker tag mysql harbor.pks.pcfdemo.com/demo/workshop-mysql
docker push harbor.pks.pcfdemo.com/demo/workshop-mysql
