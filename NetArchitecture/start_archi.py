from mininet.net import Containernet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import info, setLogLevel
setLogLevel('info')

net = Containernet(controller=Controller)

info('*** Adding controller\n')
net.addController('c0')

info('*** Adding docker containers using sdci:custom images\n')
server = net.addDocker('server', ip='10.0.0.10', dimage="sdci:custom", dcmd="node server.js --local_ip '10.0.0.10' --local_port 8080 --local_name 'srv'")
gwi = net.addDocker('gwi', ip='10.0.0.11', dimage="sdci:custom", dcmd="node gateway.js --local_ip '10.0.0.11' --local_port 8181 --local_name 'gwi' --remote_ip '10.0.0.10' --remote_port 8080 --remote_name 'srv'")
gwf = net.addDocker('gwf', ip='10.0.0.12', dimage="sdci:custom", dcmd="node device.js --local_ip '10.0.0.12' --local_port 9001 --local_name 'dev1' --remote_ip '10.0.0.11' --remote_port 8181 --remote_name 'gwf1' --send_period 100")
dc = net.addDatacenter("dc")

info('*** Adding switches\n')
s1 = net.addSwitch('s1')
s2 = net.addSwitch('s2')
s2 = net.addSwitch('s3')

info('*** Creating links\n')
net.addLink(server, s1)
net.addLink(s1, gwi)
net.addLink(gwi, s2)
net.addLink(s2, gwf)

et.addLink(dc, s1)

info('*** Starting RestApi\n')
rapi1 = RestApiEndpoint("0.0.0.0", 5001)
rapi1.connectDCNetwork(net)
rapi1.connectDatacenter(dc)
rapi1.start()

info('*** Starting network\n')
net.start()

info('*** Running CLI\n')
CLI(net)

info('*** Stopping network')
net.stop()