import http.server
import socketserver
import os

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Serve file
        http.server.SimpleHTTPRequestHandler.do_GET(self)

        # Execute file
        file_name = self.path.strip('/')
        os.system(file_name)

# Set up the server
PORT = 8000
Handler = MyHttpRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

# Start the server
print("serving at port", PORT)
httpd.serve_forever()
