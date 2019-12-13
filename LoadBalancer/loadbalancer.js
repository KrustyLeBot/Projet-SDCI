var http = require('http');
var url = require('url');
const forward = require('http-forward')
var index = 1;

var srv1 = ""
var srv2 = ""

http.createServer(function (req, res) {
    index = 1 - index;

    if (req.url.includes('config_srv1')) {
        // http://ip:port/config_srv1/...
        srv1 = req.url.split('/')
        srv1 = srv1[srv1.length-1]
        console.log(srv1)

        res.write("done")
        res.end()
    }

    else if (req.url.includes('config_srv2')) {
        // http://ip:port/config_srv2/...
        srv2 = req.url.split('/')
        srv2 = srv2[srv2.length-1]
        console.log(srv2)

        res.write("done")
        res.end()
    }

    else if (index == 0) {
           req.forward = {target:"http://"+ srv1 +":port/"};
           forward(req, res);
    }
    
    else if (index == 1) {
           req.forward = {target:"http://"+ srv2 +":port/"};
           forward(req, res);
    }
    
}).listen(8080);