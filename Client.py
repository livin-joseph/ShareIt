server_active = False

def upload(file, passwd):
    import socket
    s = socket.socket()
    port = 12345

    s.connect(('127.0.0.1', port))

    print('Message from server:', s.recv(1024).decode())
    s.send('You\'re welcome'.encode())

    print('Message from server:', s.recv(1024).decode())
    s.send('Upload'.encode())

    print('Message from server:', s.recv(1024).decode())
    s.send(passwd.encode())

    print('Message from server:', s.recv(1024).decode())
    file.seek(0, 2)
    s.send(str(file.tell()).encode())
    file.seek(0)

    print('Message from server:', s.recv(1024).decode())

    s.send(file.filename.encode())

    print('Message from server:', s.recv(1024).decode())

    s.send(file.read())

    s.close()

def download(filename, passwd):
    import socket
    s = socket.socket()
    port = 12345

    s.connect(('127.0.0.1', port))

    print('Message from server:', s.recv(1024).decode())
    s.send('You\'re welcome'.encode())

    print('Message from server:', s.recv(1024).decode())
    s.send('Download'.encode())
    
    print('Message from server:', s.recv(1024).decode())
    s.send(filename.encode())
    
    print('Message from server:', s.recv(1024).decode())
    s.send(passwd.encode())
    
    size = int(s.recv(1024).decode())

    if size == 0:
        s.close()
        from Exceptions import FileNotFoundException
        raise FileNotFoundException("File is not found in the server")
    elif size == -1:
        s.close()
        from Exceptions import WrongPasswordException
        raise WrongPasswordException("Password to access the file is incorrect")

    s.send('Got size of the file'.encode())

    filename = s.recv(1024).decode()

    s.send('Got name of the file'.encode())

    received = s.recv(size)
    with open(f'{filename}', 'wb') as file:
        file.write(received)

    print('File received from server')

    s.close()
