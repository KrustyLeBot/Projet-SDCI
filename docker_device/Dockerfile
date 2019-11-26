FROM node:alpine
WORKDIR /
ADD . /
RUN apk update \
    && npm install express \
    && npm install request \
    && wget http://homepages.laas.fr/smedjiah/tmp/device.js
ENTRYPOINT  node device.js --local_ip "127.0.0.1" --local_port 9001 --local_name "dev1" --remote_ip "127.0.0.1" --remote_port 8282 --remote_name "gwf1" --send_period 3000 ; tail -f /dev/null