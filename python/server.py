from http.server import BaseHTTPRequestHandler, HTTPServer

# Define the HTTP request handler class
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    # Override the do_GET method to handle GET requests
    def do_GET(self):
        # Send response status code
        self.send_response(200)
        # Send headers
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        # Send message back to client
        message = "Hello, World! python\n"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    # Create an HTTP server listening on the given port
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on port {port}...")
    # Run the HTTP server
    httpd.serve_forever()

# Run the server
if __name__ == "__main__":
    run()
