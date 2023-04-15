import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        return_text = ""
        if "SECRET" in self.data:
            numbers = sum(c.isdigit() for c in s)
            return_text = return_text + "Digits: Count: " + str(numbers) 
        else
            return_text = return_text + "Secret code not found."
        self.request.sendall(return_text)

if __name__ == "__main__":
    HOST, PORT = "10.10.10.2", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()