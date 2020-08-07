import socket
import sys
import math

serverip = 'localhost'#'76.176.57.74'
serverport = 8080
packetsize = 32

def inputProcessing(op, input):
    inp = op + ':' + input
    x = len(inp)+1
    size = len(str(x))
    base = pow(10, size)-size
    result = math.ceil(x/base)+x
    return str(result) + ':' + inp



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((serverip, serverport))
outmessage = inputProcessing('repeat', 'this issssssss the message')
print('outmessage= '+ outmessage)
s.send(outmessage.encode('utf-8'))

packetcount = -1
packetindex = 0

indata = b''
operation = ''
while True:
    data = s.recv(packetsize)
    packetindex+=1
    msgdata = data.decode('utf-8')
    print('packet (' + str(packetindex) + ')')
    if packetcount == -1:
        parts = msgdata.split(':')
        packetcount =  math.ceil(int(parts[0])/packetsize)
        residue = parts[1].encode('utf-8')
        indata+=residue
    else:
        indata+=data
    if packetindex == packetcount:
        break

print(indata.decode('utf-8'))
