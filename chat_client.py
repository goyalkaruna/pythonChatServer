# chat_client.py

import sys
import socket
import select
 
def chat_client():
    if(len(sys.argv) < 3) :
        print 'Usage : python chat_client.py hostname port'
        sys.exit()

    host = sys.argv[1]
    #host = socket.gethostname()
    port = int(sys.argv[2])
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    s.settimeout(2)
     
    # connect to remote host
    try :
        #s.connect(('localhost', 9009))
        s.connect((host, port))
        print "host is " + host
        print "port is "+ str(port)
    except :
        print 'Unable to connect on ' + host +" " + str(port)
        sys.exit()
     
    print 'Connected to remote host. You can start sending messages'
    sys.stdout.write('<= '); sys.stdout.flush()
     
    while 1:
        
        socket_list = [sys.stdin, s]
         
        # Get the list sockets which are readable
        ready_to_read,ready_to_write,in_error = select.select(socket_list , [], [])
         
        for sock in ready_to_read:             
            if sock == s:
                # incoming message from remote server, s
                data = sock.recv(4096)
                if not data :
                    print '\nDisconnected from chat server'
                    sys.exit()
                else :
                    #print data
                    sys.stdout.write(data)
                    sys.stdout.write('<= '); sys.stdout.flush()     
            
            else :
                # user entered a message
                msg = sys.stdin.readline()
                s.send(msg)
                sys.stdout.write('<= '); sys.stdout.flush() 

if __name__ == "__main__":

    sys.exit(chat_client())
