from socket import socket,AF_INET,SOCK_STREAM
ip="127.0.0.1"
port=4000
s=socket(AF_INET,SOCK_STREAM)
s.bind((ip,port))
s.listen(4)
c,ad=s.accept()
print('Connected from {}'.format(ad))
while True:
    data=input('Say something :') or "Hi there"
    c.send(data.encode('utf-8'))
    print(c.recv(1212).decode('utf-8'))  
