#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
import json
import time

class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    SIP Register server class
    """
    dicc = {}
    expire = ''
    lists = []

    def handle(self):
        print(self.client_address)
        request = self.rfile.read().decode('utf-8')
        print(request)
        fields = request.split(' ')

        if fields[0] == 'REGISTER':
            login = fields[1].split(':')
            self.dicc[login[1]] = self.client_address[0]

            self.expire = fields[3].split('\r')
            if int(self.expire[0]) == 0:
                del self.dicc[login[1]]

        self.register2json()
        self.wfile.write(b"SIP/2.0 200 OK " + b'\r\n\r\n')
        print(self.dicc)

    def register2json(self):


        json.dump(self.dicc, open("registered.json",'w'),
                    sort_keys=True, indent=4, separators=(',', ': '))

if __name__ == "__main__":
    try:
        PORT = int(sys.argv[1])
    except PortError:
        print("Introducir puerto escucha del servidor")
    serv = socketserver.UDPServer(('', PORT), SIPRegisterHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
