# coding=UTF-8

import socket, sys, time

# definindo endereço do servidor de destino, ip/porta
address = ('127.0.0.1', 8583)

# definindo servidor TCP para efetuar a conexão
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(address)
print '\n\tConectado ao servidor:', address

time.sleep(5)

# enviando mensagem ao servidor  
message = 'Mensagem enviado do cliente'
server.sendall(message)
print '\tEnviando: "%s"' % message

# recebendo resposta do servidor
data = server.recv(24)
while data:
  print '\tResposta: "%s"' % data
  data = server.recv(24)