rm gateway.js
rm device.js

wget http://homepages.laas.fr/smedjiah/tmp/gateway.js
wget http://homepages.laas.fr/smedjiah/tmp/device.js

node gateway.js --local_ip "${1}" --local_port 8080 --local_name "${3}" --remote_ip "${2}" --remote_port 8080 --remote_name "${4}" &

sleep 10

node device.js --local_ip "${1}" --local_port 9001 --local_name "${3}_dev1" --remote_ip "${1}" --remote_port 8080 --remote_name "${3}" --send_period $5 &
node device.js --local_ip "${1}" --local_port 9002 --local_name "${3}_dev2" --remote_ip "${1}" --remote_port 8080 --remote_name "${3}" --send_period $5 &
node device.js --local_ip "${1}" --local_port 9003 --local_name "${3}_dev3" --remote_ip "${1}" --remote_port 8080 --remote_name "${3}" --send_period $5 &
node device.js --local_ip "${1}" --local_port 9004 --local_name "${3}_dev4" --remote_ip "${1}" --remote_port 8080 --remote_name "${3}" --send_period $5 &
node device.js --local_ip "${1}" --local_port 9005 --local_name "${3}_dev5" --remote_ip "${1}" --remote_port 8080 --remote_name "${3}" --send_period $5 &
