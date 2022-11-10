#Networked programmes.
"""
Transport Control Protocol is built on top of an IP address
This protocol assumes that the IP might lose some data and would store
and retransmits the data if it seems to be lost. It does this by creating
handling the "Flow Control" using a transmit window, which provides the
a nice and reliable pipe.

Different ports would lead to different applications, such as HTTP(80) and SSH(22)
"""
#example of using TCP connection
"""
import socket  #socket is the library used to access TCP sockets

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')
mysock.close()

"""
#sockets solve the problem of application protocols such as MAIL and World Wide Web
"""
To get data from a server we need to have a GET request. When
the user presses on a link the web server would then issue a GET request for the
the page that the user requested.
"""
#Networking: Text Processing
"""
Each number is represented by a number between 0 and 256 stored
in 8 bits of memory.
"""
#We can use the ord() function to see what is the numerical representation of certain characters

#print(ord('R'))
#the numerical representation of R is 82 in ASCII.
#UTF-8 is the recommended practice for encoding data to be exchanged between systems (1-4 bytes)
"""
When we communicate with external services like network sockets we are sending bytes over,
which results in the need to encode Python 3 strings into a given character encoding.

when we read data from external services we must first decode it basied on the characters
set so it is represented correctly in Python 3 as a string.
"""
#example of this can be found here.
"""
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')
mysock.close()
"""
#Networking using urllib.
'''
Since HTTP is so common, a library exists that does all the socket processing for us
and creates a web page that looks like a file.
'''
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
