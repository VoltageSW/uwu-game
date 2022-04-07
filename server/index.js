var dgram = require('dgram');
var udpPort = process.env.UDPPORT || 3600;

var server = dgram.createSocket('udp4');
server.bind(udpPort);

server.on('listening', function(){
  console.log('Server started at ', udpPort);
});

server.on('message', function(msg, info){
  var message = msg.toString(); // need to convert to string 
  // since message is received as buffer 
  // receive the message and do task
});

server.on('error', function(){
  // handle error
});