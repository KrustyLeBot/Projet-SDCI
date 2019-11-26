FROM ubuntu:trusty
WORKDIR /
ADD . /
RUN apt-get update && apt-get install -y \
    net-tools \
    iputils-ping \
    iproute2 \
    telnet telnetd \
    iperf
    npm install express \
    npm install request \
    wget http://homepages.laas.fr/smedjiah/tmp/server.js
    
ENTRYPOINT  node server.js --local_ip "127.0.0.1" --local_port 8080 --local_name "srv" ; tail -f /dev/null