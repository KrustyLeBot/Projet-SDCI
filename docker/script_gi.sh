rm gateway.js

wget http://homepages.laas.fr/smedjiah/tmp/gateway.js

node gateway.js --local_ip "${1}" --local_port 8080 --local_name "${3}" --remote_ip "${2}" --remote_port 8080 --remote_name "srv" &