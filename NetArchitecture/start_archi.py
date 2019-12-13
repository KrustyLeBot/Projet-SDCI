from mininet.net import Containernet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import info, setLogLevel
import logging
from emuvim.dcemulator.net import DCNetwork
from emuvim.api.rest.rest_api_endpoint import RestApiEndpoint
from emuvim.api.tango import TangoLLCMEndpoint
import time

setLogLevel('info')

net = DCNetwork(monitor=False, enable_learning=True)

X = "krustylebot/repo:sdci_containernet"

info('*** Adding docker containers using krustylebot/repo:sdci_containernet images\n')
test = net.addDocker('test', ip='10.0.0.9', dimage=X)
server = net.addDocker('server', ip='10.0.0.10', dimage=X, dcmd="sh -c 'cd /Projet-SDCI/docker && git pull && sh script_server.sh 10.0.0.10; tail -f /dev/null'")
gwi = net.addDocker('gwi', ip='10.0.0.11', dimage=X, dcmd="sh -c 'cd /Projet-SDCI/docker && git pull && sh script_gi.sh 10.0.0.11 10.0.0.10; tail -f /dev/null'")
gwf = net.addDocker('gwf', ip='10.0.0.12', dimage=X, dcmd="sh -c 'cd /Projet-SDCI/docker && git pull && sh script_gf.sh 10.0.0.12 10.0.0.11; tail -f /dev/null'")
dc = net.addDatacenter("dc")

info('*** Adding switches\n')
s1 = net.addSwitch('s1')

info('*** Creating links\n')
net.addLink(test, s1, delay="20ms")
net.addLink(server, s1, delay="20ms")
net.addLink(gwi, s1, delay="20ms")
net.addLink(gwf, s1, delay="20ms")

net.addLink(dc, s1, delay="20ms")

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