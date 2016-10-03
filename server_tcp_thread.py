# coding=UTF-8

import socket, thread

# definindo endereço do servidor, ip/porta
address = ('127.0.0.1', 8583)

# definindo função para tratar de cada cliente separadamente
def connected(connection, client):
  print '\n\tConectador por:', client

  while True:

    # recebendo a mensagem
    message = connection.recv(1024)
    if not message: break
    print '\tNova mensagem de: %s, "%s"' % (client, message)

    # enviando a resposta
    response = 'Resposta do servidor, do servidor, do servidor, do servidor'
    connection.sendall(response)
    print '\tRespondendo ao: %s, "%s"' % (client, response)
    connection.close()
    thread.exit()

# definindo servidor TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen(True)

# aguardando clientes se conectarem
while True:
  connection, client = server.accept()
  thread.start_new_thread(connected, tuple([connection, client]))

server.close();