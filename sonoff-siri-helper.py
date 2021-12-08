from zeroconf import ServiceBrowser, Zeroconf
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

#replace with the device hostname (default: raspberrypi.local)
#TODO: get hostname programatically
hostName = "sonoff-siri-helper.local"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    sonoffIP = "defValue"
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(self.sonoffIP, "utf-8"))
        print("sonoff IP: %s" % (self.sonoffIP))

class MyListener:

    def remove_service(self, zeroconf, type, name):
        print("Service %s removed" % (name,))

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        if info: 
            MyServer.sonoffIP="http://"+socket.inet_ntoa(info.addresses[0])
            MyServer.sonoffIP+=":8081/zeroconf/switch"
            print("Service %s added, IP address: %s" % (name, MyServer.sonoffIP))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        zeroconf = Zeroconf()
        listener = MyListener()
        browser = ServiceBrowser(zeroconf, "_ewelink._tcp.local.", listener)
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    zeroconf.close()
    webServer.server_close()
    print("Server stopped.")