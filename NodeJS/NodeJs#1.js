/*
#1
var http = require('http');

var server = http.createServer(function (req, res) {
    res.end("Hi, selamat datang di nodejs");
});

server.listen(8000);

console.log("server running on http://localhost:8000");
#2
var http = require('http')
var dt = require('./myfirstmodule')

http.createServer(function(req, res){
	res.writeHead(200,{'Content-Type':'text/html'});
	res.write('The date and time are currently: ' + dt.myDateTime());
	res.end();
}).listen(8080);
#3
var http = require('http')
var fs = require('fs')

http.createServer(function(req, res){
	fs.readFile('demofile.html', function(err,data){
		res.writeHead(200,{'Content-Type':'text/html'});
		res.write(data);
		return res.end();
	});
}).listen(8080);
#4
var url = require('url');
var adr = 'http://localhost:8080/default.htm?year=2022&month=March';
var q = url.parse(adr, true);

console.log(q.host); //returns 'localhost:8080'
console.log(q.pathname); // returns 'default.htm'
console.log(q.search); //returns 'year=2022&month=March'

var qdata = q.query;
console.log(qdata.month);
*/
