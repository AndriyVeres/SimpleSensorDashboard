from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = "127.0.0.1"
PORT = 9999
BGCOLOR = "black"
COLOR = "red" # yellow, chartreuse
TEMP=22

class Dashboard(BaseHTTPRequestHandler):

	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()

		self.wfile.write(bytes(
			"<html>\
				<body bgcolor=\"" + BGCOLOR + "\">\
   					<style>\
        				.header{\
        					font-size: 320px;\
        					line-height: 1px;\
        					color: " + COLOR + ";\
        					text-align: center;\
     					}\
     				</style>\
					<div class=\"header\">\
    					<h1>" + str(TEMP) + "</h1>\
					</div>\
				</body>\
			</html>",
			"utf-8"))

server = HTTPServer((HOST, PORT), Dashboard)
print("Running")
server.serve_forever()
server.server_close()
print("Stop")