import socket 
import sys
import argparse

host = '192.168.0.104'

def echo_client(port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_address = (host,port)
    print("[*]:Connecting to %s port %s" % server_address)
    sock.connect(server_address)
    message = str(input("[*]:Say something : "))
    try:
        print("[*]:Sending %s" % message)
        sock.sendall(message.encode('utf-8'))
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(1024)
            amount_received += len(data)
            print("[*]:Received : %s" % data.decode('utf-8'))
    except socket.error as e:
        print("Socket error : %s " % str(e))
    except Exception as e:
        print("Other exception : %s" % str(e))
    finally:
        print("[*]:Closing connection to the server ")
        sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port',action="store",dest="port",type=int,required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_client(port)
