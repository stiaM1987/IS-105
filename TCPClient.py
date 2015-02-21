from socket import *
serverName = 'servername'
serverPort = 1200
clientSocket = socket (AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = raw_input('Input lowercase sentence:')
clientSocket.send(sentence)
modifiedSentence = clientSocket.recv(1024)
print 'Fromserver:', modifiedSentence
clientSocket.close()
