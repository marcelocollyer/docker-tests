require 'webrick'

# Create a new class that extends WEBrick::HTTPServlet::AbstractServlet
class SimpleServlet < WEBrick::HTTPServlet::AbstractServlet
  def do_GET(request, response)
    response.status = 200
    response['Content-Type'] = 'text/html'
    response.body = '<html><body><h1>Hello, World!</h1></body></html>'
  end
end

# Create a new instance of WEBrick::HTTPServer, listening on port 8000
server = WEBrick::HTTPServer.new(:Port => 8000)

# Mount our SimpleServlet class to the root URL path
server.mount('/', SimpleServlet)

# Trap signals to gracefully shut down the server
trap('INT') { server.shutdown }

# Start the server
server.start
