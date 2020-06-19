import socket
import sys

serverip = 'localhost'#'76.176.57.74'
serverport = 8080
packetsize = 32

def inputProcessing(op, input):
    inp = op + ':' + input
    outlen = int(len(inp.encode('utf-8'))/packetsize)
    outlen+=len(str(outlen))
    return str(outlen) + ':' + inp



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((serverip, serverport))
outmessage = inputProcessing('repeat', 'this is sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssthe message')
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
        packetcount = int(parts[0])
        residue = parts[1].encode('utf-8')
        indata+=residue
    else:
        indata+=data
    if packetindex == packetcount:
        break

print(indata.decode('utf-8'))
