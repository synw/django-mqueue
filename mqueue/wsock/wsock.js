var PORT = 3000;
var HOST = 'localhost';

var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var path = require("path");
var socket = io

var redis = require('redis');
var client = redis.createClient(6379, "localhost");
var client2 = redis.createClient(6379, "localhost");

app.get('/', function(req, res){
	var key = req.query.k;
	socket.on('connect', function(socket) {
		console.log('connect');
		if ( key !== 'p' ) {
			client2.get(key, function(err, reply) {
				console.log('Reply: '+reply);
				client2.del(key);
				if (reply == 'admin') {
					socket.join('admin');
					socket.join('staff');
					socket.join('user');
				}
				else if (reply == 'staff') {
					socket.join('staff');
					socket.join('user');
				}
				else if (reply == 'user') {
					socket.join('user');
				}
			});
		}
	});
	res.sendFile(path.join(__dirname+'/public/index.html'));
});

client.subscribe("public");
client.subscribe("user");
client.subscribe("staff");
client.subscribe("admin");
	
client.on("message", function(channel, message){
	console.log(channel + ": " + message);
	var msg = message;
	if ( channel == 'admin' ) {
		msg = message+'#!#admin';
		io.to('admin').emit("message", msg);
	}
	else if ( channel == 'staff' ) {
		msg = message+'#!#staff';
		io.to('staff').emit("message", msg);
	}
	else if ( channel == 'user' ) {
		msg = message+'#!#user';
		io.to('user').emit("message", msg);
	}
	else if ( channel == 'public' ) {
		msg = message+'#!#public';
		io.emit("message", msg);
	}
});

http.listen(PORT, function(){
	console.log('listening on *:'+PORT);
});






