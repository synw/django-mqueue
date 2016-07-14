// config
var REDIS_PORT = 6379;
var REDIS_HOST = 'localhost'
var PORT = 3000; 
var DEBUG = true;
var SITE_SLUG = 'localsite'
var GLOBAL_CHANNELS = ['admin']

// imports
var app = require('express')();
var http = require('http').Server(app);
var socket = require('socket.io')(http);
var path = require("path");

// redis client
var redis = require('redis');
var client = redis.createClient(REDIS_PORT, REDIS_HOST);
var client2 = redis.createClient(REDIS_PORT, REDIS_HOST);

//get channels names for site
var admin_channel = SITE_SLUG+'_'+'admin';
var staff_channel = SITE_SLUG+'_'+'staff';
var user_channel = SITE_SLUG+'_'+'user';
var public_channel = SITE_SLUG+'_'+'public';
for ( i = 0; i < GLOBAL_CHANNELS.length; i ++ ) {
	if ( GLOBAL_CHANNELS[i] == 'admin' ) {
		admin_channel = 'admin';
	}
	if ( GLOBAL_CHANNELS[i] == 'staff' ) {
		staff_channel = 'staff';
	}
	if ( GLOBAL_CHANNELS[i] == 'user' ) {
		user_channel = 'user';
	}
	if ( GLOBAL_CHANNELS[i] == 'public' ) {
		public_channel = 'public';
	}
}
if (DEBUG === true) {
	console.log('Admin channel : '+admin_channel);
	console.log('Staff channel : '+staff_channel);
	console.log('User channel : '+user_channel);
	console.log('Public channel : '+public_channel);
}

// server
app.get('/', function(req, res){
	var key = req.query.k;
	socket.on('connect', function(socket) {
		if (DEBUG === true) {
			console.log('* Connection');
			console.log('key -> '+key)
		}
		if ( key == null ) {
			socket.disconnect();
			if (DEBUG === true) {
				console.log('* Disconnection : no key provided');
			}
		}
		if ( key !== 'p' && typeof key != 'undefined' && key !== null ) {
			client2.hgetall(key, function(err, reply) {
				if (reply !== null) {
					var user_class = reply['user_class'];
					var username = reply['username'];
					if (DEBUG === true) {
						console.log(user_class+' user '+username+' connected');
					}
					client2.del(key);
					if (user_class == 'admin') {
						socket.join(admin_channel);
						socket.join(staff_channel);
						socket.join(user_channel);
						if (DEBUG === true) {
							console.log('OK: Admin user joined channels '+admin_channel+', '+staff_channel+', '+user_channel);
						}
					}
					else if (user_class == 'staff') {
						socket.join(staff_channel);
						socket.join(user_channel);
						if (DEBUG === true) {
							console.log('OK: Staff user joined channels '+staff_channel+', '+user_channel);
						}
					}
					else if (user_class == 'user') {
						socket.join(user_channel);
						if (DEBUG === true) {
							console.log('OK: Logged in user joined channel '+user_channel);
						}
					}
				}
			});
		}
		else {
			if (DEBUG === true) {
				user_class = 'anonymous';
				username = 'anonymous';
				console.log('OK: Anonymous user connected');
			}
		}
	});
	res.sendFile(path.join(__dirname+'/public/index.html'));
});

//channel subscriptions
client.subscribe(public_channel);
client.subscribe(user_channel);
client.subscribe(staff_channel);
client.subscribe(admin_channel);
	
// listener
client.on("message", function(channel, message){
	var l=message.split('#!#');
	var msg = l[0]
	var event_class = l[1]
	if (DEBUG === true) {
		console.log('MESSAGE ('+event_class+'): '+channel + ": " + msg);
	}
	if ( channel == admin_channel ) {
		data = { 'message':msg, 'channel':'admin', 'event_class':event_class};
		socket.to(admin_channel).emit("message", data);
	}
	else if ( channel == staff_channel ) {
		data = { 'message':msg, 'channel':'staff', 'event_class':event_class};
		socket.to(staff_channel).emit("message", data);
	}
	else if ( channel == user_channel ) {
		data = { 'message':msg, 'channel':'user', 'event_class':event_class};
		socket.to(user_channel).emit("message", data);
	}
	else if ( channel == public_channel ) {
		data = { 'message':msg, 'channel':'public', 'event_class':event_class};
		socket.emit("message", data);
	}
});

// runtime
http.listen(PORT, function(){
	if (DEBUG === true) {
		console.log('listening on *:'+PORT);
	}
});






