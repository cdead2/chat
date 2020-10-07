from socket import socket,AF_INET,SOCK_STREAM
s=socket(AF_INET,SOCK_STREAM)
ip='77.69.189.10'
port=4000
s.connect((ip,port))
while True:
    print(s.recv(1213).decode('utf-8'))
    data=input('Say something : ')or 'Hi'
    s.send(data.encode('utf-8'))    
