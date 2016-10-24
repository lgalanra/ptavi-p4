#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import socket
import sys


if __name__ == "__main__":
# Constantes. Dirección IP del servidor y contenido a enviar
    try:
        SERVER = sys.argv[1]
        PORT = int(sys.argv[2])
        register = sys.argv[3]
        direction = sys.argv[4]
    except ValueError:
        sys.exit("Llamada incorrecta al programa")

    # Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
        my_socket.connect((SERVER, PORT))

        if sys.argv[3] == 'register':
            my_socket.send(bytes('REGISTER sip:' + sys.argv[4] +' SIP/2.0','utf-8')
                            + b'\r\n\r\n')

        data = my_socket.recv(1024)
        print(data.decode('utf-8'))

        print("Socket terminado.")
