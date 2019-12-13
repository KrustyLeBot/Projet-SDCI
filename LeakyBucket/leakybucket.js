var http = require('http');
var url = require('url');
const forward = require('http-forward')

var buffer = []
var srv = ""

http.createServer(function (req, res) {
    
    if (req.url.includes('config_srv')) {
        // http://ip:port/config_srv/...
        srv = req.url.split('/')
        srv = srv[srv.length-1]
        console.log(srv1)

        res.write("done")
        res.end()
    }

    else {
        buffer.push([req,res])

        req.forward = {target:"http://"+ srv2 +":port/"};
           forward(req, res);
    }
    
}).listen(8080);
