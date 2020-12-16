import socket 
import sys
import argparse
from _thread import *
from tqdm import tqdm
import time
from time import sleep

host = ''
data_payload = 2048
backlog = 5



def thread(c,a): 
    data = c.recv(data_payload)
    address = str(a)
    try:
        if data:
            print("[*]:Data = %s " % data.decode('utf-8'))
            c.sendall(data)
            print("[*]:Sent %s bytes back to "% (data.decode()) + address)
    finally:
        print("Close the connection")
        c.close()

def echo(port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #create tcp socket
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)  #enable reuse address/port
    server_address = (host,port)
    threadCount = 0 
    word = "\t \t \t Welcome to the echo server \n"
    for char in word:
        sleep(0.055)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("[*]:Starting up echo server on %s port %s" % server_address)
    sock.bind(server_address)
    sock.listen(backlog)  #listen to clients,backlog argument specifies the max no. of queued connections     
    while True: 
        print("[*]:Waiting to receive message from the client") 
        client, address = sock.accept()
        for i in tqdm(range(10),desc="Connecting...",ascii=False,ncols=75):
            time.sleep(0.012)
        #print("Complete")
        threadCount += 1
        print("----------------------------------------------------------------------------")
        print("Thread number :"+ str(threadCount))
        print("[*]:Got connection from " + address[0] + ':' + str(address[1]))
        start_new_thread(thread, (client,address))
               
#def quit(q):
    #if q == 'quit':
        #sys.exit()
        #sock.close()
        
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port',action="store", dest="port",type=int,required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo(port)
    #quit = thread()
    #quit(quit)
