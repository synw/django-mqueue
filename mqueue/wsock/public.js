var PORT = 3000;
var HOST = 'localhost';

var express = require('express');
var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var path = require("path");
var socket = io

var redis = require('redis');
var client = redis.createClient(6379, "localhost");
var client2 = redis.createClient(6379, "localhost");

app.get('/', function(req, res){	
	res.sendFile(path.join(__dirname+'/public/index.html'));
});

client.subscribe("public");
	
client.on("message", function(channel, message){
	console.log(channel + ": " + message);
	socket.emit("message", message);
});

http.listen(PORT, function(){
	console.log('listening on *:'+PORT);
});




