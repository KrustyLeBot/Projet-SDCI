rm server.js

wget http://homepages.laas.fr/smedjiah/tmp/server.js

node server.js --local_ip "${1}" --local_port 8080 --local_name "srv" &