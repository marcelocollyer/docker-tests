const http = require('http');

// Create an HTTP server
const server = http.createServer((req, res) => {
  // Set response headers
  res.writeHead(200, {'Content-Type': 'text/plain'});
  // Send the response body
  res.end('Hello, World! node\n');
});

// Define the port to listen on
const port = 8001;

// Start the server and listen on the specified port
server.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});