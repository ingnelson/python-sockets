import socket
import sys
import threading
import math

serverport = 8080
packetsize = 32


def serverProcessing(op, bytearr, addr):
    if op=='repeat':
        return bytearr

def inputProcessing(input):
    x = len(input)+1
    size = len(str(x))
    base = pow(10, size)-size
    result = math.ceil(x/base)+x
    return str(result) + ':' + input

def serverwaiter():
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.bind(('',serverport))
    s.listen(10)
    print('initialized server')
    while True:
        cobj,addr = s.accept()
        print('client connected')
        mythread = threading.Thread(target=client,name='TCP client {}'.format(threading.active_count()-1),args=(cobj,addr))
        mythread.daemon = True # So client threads die on main thread exit.
        mythread.start()

def client(cobj,addr):
    print('Connected to',addr)
    packetcount = -1
    packetindex = 0

    indata = b''
    operation = ''
    while True:
        data = cobj.recv(packetsize)
        packetindex+=1
        msgdata = data.decode('utf-8')
        print('packet (' + str(packetindex) + ')')
        if packetcount == -1:
            parts = msgdata.split(':')
            packetcount = math.ceil(int(parts[0])/packetsize)
            operation = parts[1]
            residue = parts[2].encode('utf-8')
            indata+=residue
        else:
            indata+=data


        if packetindex == packetcount:
            break
    msgout = serverProcessing(operation, indata, addr)
    cobj.send(inputProcessing(msgout.decode('utf-8')).encode('utf-8'))
    print('client closed')
    cobj.close()

serverwaiter()
