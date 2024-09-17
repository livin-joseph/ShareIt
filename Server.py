def server():
    import socket
    s = socket.socket()
    port = 12345
    buffer = []

    s.bind(('127.0.0.1', port))
    print("Socket binded to", port)

    s.listen(10)
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

            c.send('Send name of the file'.encode())

            filename = c.recv(1024).decode()
            print(f'Name of the file: {filename}')

            c.send('Send the file'.encode())

            received = c.recv(size)

            '''
            # To save the received bytestream as a file
            with open('Flask/goat.jpg', 'wb') as file:
                file.write(received)
            '''

            buffer.append((size, filename, received))

            c.close()
            print('File received from client')

        elif msg == 'Download': # Client download - server upload
            if len(buffer) > 0:
                t = buffer.pop(0)
                c.send(str(t[0]).encode())

                print('Message from client:', c.recv(1024).decode())

                c.send(t[1].encode())

                print('Message from client:', c.recv(1024).decode())

                c.send(t[2])

                c.close()
                print('File sent to client')
            else:
                c.send('0'.encode())

                c.close()
                print('Buffer is empty')

        else:
            c.close()
            print('Server is stopped')
            break

server()
