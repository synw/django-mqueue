var PORT = 3001;
var HOST = 'localhost';

var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var cookie_reader = require('cookie');
var path = require("path");
var socket = io

var redis = require('redis');
var client = redis.createClient(6379, "localhost");
var client2 = redis.createClient(6379, "localhost");

app.get('/', function(req, res){
	key = req.query.k
	socket.on('connect', function(socket) {
		//console.log('connect')
	  	client2.get(key, function(err, reply) {
		    //console.log(key+' - Reply: '+reply+' / '+err);
		    client2.del(key);
		    if (reply != 'admin') {
		    	socket.disconnect(true);
		    }
		});
	});	
	res.sendFile(path.join(__dirname+'/public/index.html'));
});

client.subscribe("public");
client.subscribe("admin");
	
client.on("message", function(channel, message){
	console.log(channel + ": " + message);
	var msg = message;
	if ( channel == 'admin' ) {
		msg = message+'#!#admin';
	}
	socket.emit("message", msg);
});

http.listen(PORT, function(){
	console.log('listening on *:'+PORT);
});






