FROM node:alpine
WORKDIR /
ADD . /
RUN apk update \
    && npm install express \
    && npm install request \
    && wget http://homepages.laas.fr/smedjiah/tmp/server.js
ENTRYPOINT  node server.js --local_ip "127.0.0.1" --local_port 8080 --local_name "srv" ; tail -f /dev/null