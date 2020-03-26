var express = require("express");
var app = express();
var server = require('http').createServer(app);

app.get('/', function (req, res, ext) {
    res.sendFile(__dirname + '/public/index.html');
});

app.use(express.static('public'));

server.listen(8000);