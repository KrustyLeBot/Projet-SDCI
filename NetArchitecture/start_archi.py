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
d1 = net.addDocker('d1', dimage="sdci:custom")
d2 = net.addDocker('d2', dimage="sdci:custom")
dc = net.addDatacenter("dc")

info('*** Adding switches\n')
s1 = net.addSwitch('s1')
s2 = net.addSwitch('s2')

info('*** Creating links\n')
net.addLink(d1, s1)
net.addLink(s1, s2)
net.addLink(s2, d2)

et.addLink(dc, s1)

info('*** Starting RestApi\n')
rapi1 = RestApiEndpoint("0.0.0.0", 5001)
rapi1.connectDCNetwork(net)
rapi1.connectDatacenter(dc)
rapi1.start()

info('*** Starting network\n')
net.start()

info('*** Testing connectivity\n')
net.ping([d1, d2])

info('*** Running CLI\n')
CLI(net)

info('*** Stopping network')
net.stop()