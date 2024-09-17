def server():
    import socket
    s = socket.socket()
    port = 12345
    buffer = []

    s.bind(('127.0.0.1', port))
    print("Socket binded to", port)

    s.listen(5)
    print("Socket is listening")

    while True:
        c, addr = s.accept()
        print('Got connection from', addr)

        c.send('Thank you for connecting'.encode())
        print('Message from client:', c.recv(1024).decode())

        c.send('Upload or Download or Stop'.encode())
        msg = c.recv(1024).decode()
        print('Message from client:', msg)

        if msg == 'Upload': # Client upload - server download
            c.send('Send size of the file'.encode())

            size = int(c.recv(1024).decode())
            print(f'Size of the file: {size} bytes')

            c.send('Send the file'.encode())

            received = c.recv(size)
            '''
            with open('Flask/goat.jpg', 'wb') as file:
                file.write(received)
            '''
            buffer.append((size, received))

            c.close()
            print('File received from client')

        elif msg == 'Download': # Client download - server upload
            if len(buffer) > 0:
                t = buffer.pop(0)
                c.send(str(t[0]).encode())

                print('Message from client:', c.recv(1024).decode())

                c.send(t[1])

                c.close()
                print('File sent to client')
            else:
                print('Buffer is empty')

        else:
            c.close()
            print('Server is stopped')
            break
server()
