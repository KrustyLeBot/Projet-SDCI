var express = require('express')
var app = express()
app.use(express.json()) // for parsing application/json
var request = require('request');
const si = require('systeminformation');

var offset = 0.0;


function monitor(ip, port) {
    console.log('ip : ' + ip );
    console.log('port : ' + port );
    const start = Date.now();
    request("http://" + ip + ":" + port + "/ping");
    return Date.now() - start;
}


app.get('/monitor/:ip/:port', function(req, res) {
    var ip= req.params.ip;
    var port = req.params.port;
    var i;
    var delay = 0;
    for(i = 0; i<100; i++){
    	delay += monitor(ip, port);
    }
    delay = offset + (delay/100.0);

    res.write(delay.toString());
    res.end();
});

app.get('/ping', function(req, res) {
    console.log('ping recu');
    res.write("Pong");
    res.end();
});

app.get('/offset/:valeur', function(req, res) {
    offset = req.params.valeur;
    res.write("Done");
    res.end();
});

app.listen(8080 , function () {
    console.log('listening on : ' + 8080 );
});