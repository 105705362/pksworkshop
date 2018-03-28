docker rm rest-crud -f
docker build . -t rest-crud
docker run --name rest-crud -p5000:5000 -d rest-crud
