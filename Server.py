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
            c.send('Send password to access the file'.encode())
            passwd = c.recv(1024).decode()

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

            buffer.append((passwd, size, filename, received))

            c.close()
            print('File received from client')

        elif msg == 'Download': # Client download - server upload
            c.send('Send name of the file'.encode())
            filename = c.recv(1024).decode()

            c.send('Send password to access the file'.encode())
            password = c.recv(1024).decode()

            file_copy = None
            WrongPasswordFlag = False
            if len(buffer) > 0:
                for i in buffer:
                    if i[2] == filename:
                        file_copy = i
                        print('File is found')
                        if password != file_copy[0]:
                            c.send('-1'.encode())
                            c.close()
                            print('Incorrect password')
                            WrongPasswordFlag = True
                        else:
                            c.send(str(file_copy[1]).encode())
                            print('Correct password')
                        break
                else:
                    c.send('0'.encode())
                    c.close()
                    print('File is not found')
                    continue
            else:
                c.send('0'.encode())
                c.close()
                print('File is not found')
                continue

            if WrongPasswordFlag == True:
                continue

            buffer.remove(file_copy)

            print('Message from client:', c.recv(1024).decode())

            c.send(file_copy[2].encode())

            print('Message from client:', c.recv(1024).decode())

            c.send(file_copy[3])

            c.close()
            print('File sent to client')

        else:
            c.close()
            print('Server is stopped')
            break

if __name__ == '__main__':
    server()
