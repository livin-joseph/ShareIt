def upload(loc=''):
    import socket
    s = socket.socket()
    port = 12345

    s.connect(('127.0.0.1', port))

    loc = 'Flask/dhoni.jpg'

    print('Message from server:', s.recv(1024).decode())
    s.send('You\'re welcome'.encode())

    print('Message from server:', s.recv(1024).decode())
    s.send('Upload'.encode())

    print('Message from server:', s.recv(1024).decode())

    import os
    size = os.path.getsize(loc)
    s.send(str(size).encode())

    print('Message from server:', s.recv(1024).decode())

    with open(loc, 'rb') as file:
        s.send(file.read())

    s.close()

def download():
    import socket
    s = socket.socket()
    port = 12345

    s.connect(('127.0.0.1', port))

    print('Message from server:', s.recv(1024).decode())
    s.send('You\'re welcome'.encode())

    print('Message from server:', s.recv(1024).decode())
    s.send('Download'.encode())
    
    size = int(s.recv(1024).decode())
    s.send('Got size of the file'.encode())

    received = s.recv(size)
    with open('Flask/goat.jpg', 'wb') as file:
        file.write(received)

    print('File received from server')

    s.close()

def stop():
    import socket
    s = socket.socket()
    port = 12345

    s.connect(('127.0.0.1', port))

    print('Message from server:', s.recv(1024).decode())
    s.send('You\'re welcome'.encode())

    print('Message from server:', s.recv(1024).decode())
    s.send('Stop'.encode())

    s.close()
