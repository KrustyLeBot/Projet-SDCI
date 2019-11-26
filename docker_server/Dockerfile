FROM node:alpine
WORKDIR /
ADD . /
RUN apk update \
    && npm install express \
    && npm install request \
    && wget http://homepages.laas.fr/smedjiah/tmp/gateway.js
ENTRYPOINT  node gateway.js --local_ip "127.0.0.1" --local_port 8181 --local_name "gwi" --remote_ip "127.0.0.1" --remote_port 8080 --remote_name "srv" ; tail -f /dev/null