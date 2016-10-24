#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys


class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        self.wfile.write(b"Hemos recibido tu peticion")
        print(self.client_address[0])
        print(self.client_address[1])
        for line in self.rfile:
            print("El cliente nos manda ", line.decode('utf-8'))

if __name__ == "__main__":
    try:
        PORT = int(sys.argv[1])
    except PortError:
        print("Introducir puerto escucha del servidor")
    serv = socketserver.UDPServer(('', PORT), EchoHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
