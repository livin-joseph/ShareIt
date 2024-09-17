def upload(file=None):
    import socket
    s = socket.socket()
    port = 12345

    s.connect(('127.0.0.1', port))

    print('Message from server:', s.recv(1024).decode())
    s.send('You\'re welcome'.encode())

    print('Message from server:', s.recv(1024).decode())
    s.send('Upload'.encode())

    print('Message from server:', s.recv(1024).decode())

    file.seek(0, 2)
    s.send(str(file.tell()).encode())
    file.seek(0)

    print('Message from server:', s.recv(1024).decode())

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
    with open('goat.jpg', 'wb') as file:
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
