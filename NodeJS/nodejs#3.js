/*
//WebStatis

var http = require('http');
var url = require('url');
var fs = require('fs');

http.createServer(function(req, res){
	var q = url.parse(req.url, true);
	var filename = "." + q.pathname;
//baca file
	fs.readFile(filename, function(err, data){
		if (err){ //kirim balasan error
			res.writeHead(404,{'Content-Type': 'text/html'});
			return res.end("404 Not Found")
		}
//kirim balasan dengan file statis
		res.writeHead(200, {'Content-Type': 'text/html'});
		res.write(data);
		return res.end();
	});
}).listen(8000);

*/

//FormGet

var http = require('http')
var url = require('url')
var fs = require('fs')

http.createServer(function(req, res){
	var q = url.parse(req.url, true);

	if(q.pathname =="/search/" && req.method === "GET"){
			//mengambil parameter dari URL
		var keyword = q.query.keyword;
		if(keyword){
			//mengambil data dari form dengan metode GET
			res.writeHead(200, {'Content-Type': 'text/html'});
			res.write("<h3>Search Results:</h3>");
			res.write("<p>Anda Mencari:<b>"+ keyword +"</b></p>");
			res.write("<pre>Maaf Yaa.. <br/>kata tidak ditemukan");
			res.end("<a href='/search/'> Kembali Pulang</a>");
		} else{
			//tampilkan form search
		fs.readFile('nodejs3.html', (err, data) => {
			if (err){ //kirim balasan error
				res.writeHead(404, {'Content-Type': 'text/html'});
				return res.end("404 Not Found");
			}
			//kirim form search.html
			res.writeHead(202, {'Content-Type': 'text/html'});
			res.write(data);
			return res.end();
		});

		}

	}
}).listen(2022);