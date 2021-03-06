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
server = net.addDocker('server', ip='10.0.0.10', dimage=X, dcmd="sh -c 'cd /Projet-SDCI/docker && git pull && sh script_server.sh 10.0.0.10; tail -f /dev/null'")
gwi1 = net.addDocker('gwi1', ip='10.0.0.11', dimage=X, dcmd="sh -c 'cd /Projet-SDCI/docker && git pull && sh script_gi.sh 10.0e.0.11 10.0.0.10 gwi1; tail -f /dev/null'")
gwf1 = net.addDocker('gwf1', ip='10.0.0.12', dimage=X, dcmd="sh -c 'cd /Projet-SDCI/docker && git pull && sh script_gf.sh 10.0.0.12 10.0.0.11 gwf1 gwi1 300; tail -f /dev/null'")
gwf2 = net.addDocker('gwf2', ip='10.0.0.13', dimage=X, dcmd="sh -c 'cd /Projet-SDCI/docker && git pull && sh script_gf.sh 10.0.0.13 10.0.0.11 gwf2 gwi1 300; tail -f /dev/null'")
gwf3 = net.addDocker('gwf3', ip='10.0.0.14', dimage=X, dcmd="sh -c 'cd /Projet-SDCI/docker && git pull && sh script_gf.sh 10.0.0.14 10.0.0.11 gwf3 gwi1 300; tail -f /dev/null'")

monitoring = net.addDocker('monitoring', ip='10.0.0.15', dimage=X, dcmd="sh -c 'cd /Projet-SDCI && git pull; cd Monitoring; sh monitoring.sh; tail -f /dev/null'")

dc = net.addDatacenter("dc")

info('*** Adding switches\n')
s1 = net.addSwitch('s1')

info('*** Creating links\n')
net.addLink(server, s1, delay="20ms")
net.addLink(gwi1, s1, delay="20ms")
net.addLink(gwf1, s1, delay="20ms")
net.addLink(gwf2, s1, delay="20ms")
net.addLink(gwf3, s1, delay="20ms")
net.addLink(monitoring, s1, delay="20ms")
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