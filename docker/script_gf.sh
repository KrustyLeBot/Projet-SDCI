rm gateway.js
rm device.js

wget http://homepages.laas.fr/smedjiah/tmp/gateway.js
wget http://homepages.laas.fr/smedjiah/tmp/device.js

node gateway.js --local_ip "${1}" --local_port 8181 --local_name "gwf" --remote_ip "${2}" --remote_port 8080 --remote_name "gwi1"

node device.js --local_ip "${1}" --local_port 9001 --local_name "dev1" --remote_ip "${1}" --remote_port 8181 --remote_name "gwf1" --send_period 100
node device.js --local_ip "${1}" --local_port 9002 --local_name "dev2" --remote_ip "${1}" --remote_port 8181 --remote_name "gwf1" --send_period 100
node device.js --local_ip "${1}" --local_port 9003 --local_name "dev3" --remote_ip "${1}" --remote_port 8181 --remote_name "gwf1" --send_period 100
node device.js --local_ip "${1}" --local_port 9004 --local_name "dev4" --remote_ip "${1}" --remote_port 8181 --remote_name "gwf1" --send_period 100
node device.js --local_ip "${1}" --local_port 9005 --local_name "dev5" --remote_ip "${1}" --remote_port 8181 --remote_name "gwf1" --send_period 100