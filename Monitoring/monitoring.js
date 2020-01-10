var express = require('express')
var app = express()
app.use(express.json()) // for parsing application/json
var request = require('request');
const si = require('systeminformation');


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
    for(i = 0; i<10; i++){
    	delay += monitor(ip, port);
    }
    res.write(delay/10.0);
});

app.listen(8686 , function () {
    console.log('listening on : ' + 8686 );
});