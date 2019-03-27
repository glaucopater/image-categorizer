fs = require('fs');
http = require('http');
url = require('url');
const SERVER_PORT = '8080';
const SERVER_URL = '127.0.0.1';

console.log(`Server listening on ${SERVER_URL}:${SERVER_PORT}` );

http.createServer(function(req, res){
  var request = url.parse(req.url, true);
  var action = request.pathname;

  if (action.indexOf(".jpg") > -1) {
      console.log(action);
      try {
        var img = fs.readFileSync("." + action);
        res.writeHead(200, {'Content-Type': 'image/jpeg' });
        res.end(img, 'binary');
      }
      catch (e) {
        console.log("Cannot read file :" + action);
      }

  } else { 
    fs.readFile('demofile1.html', function(err, data) {
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.write(data);
        res.end();
      });
  }

}).listen(SERVER_PORT, SERVER_URL);