from socket  import *
from constCS import * #-

s = socket(AF_INET, SOCK_STREAM) 
s.bind((HOST, PORT))  #-
s.listen(1)           #-
(conn, addr) = s.accept()  # returns new socket and addr. client 
while True:                # forever
  data = conn.recv(1024)   # receive data from client
  if not data: break       # stop if client stopped
  print(bytes.decode(data))
  valor = bytes.decode(data)
  for i in range(len(valor)):
                 if valor[i] == '+' or valor[i] == '-' or valor[i] == '*' or valor[i] == '/':
                   operacao = i
  if valor[operacao] == '+':
    num1 = int(valor[:operacao])
    num2 = int(valor[operacao+1:])
    total = num1 + num2
    conn.send(str.encode(str(total))) # return sum of two numbers sent from client
  elif valor[operacao] == '-':
    num1 = int(valor[:operacao])
    num2 = int(valor[operacao+1:])
    total = num1 - num2
    conn.send(str.encode(str(total))) # return substraction of two numbers sent by client
  elif valor[operacao] == '*':
    num1 = int(valor[:operacao])
    num2 = int(valor[operacao+1:])
    total = num1 * num2
    conn.send(str.encode(str(total))) # return multiplication of two numbers sent by client
  elif valor[operacao] == '/':
    num1 = int(valor[:operacao])
    num2 = int(valor[operacao+1:])
    total = num1 / num2
    conn.send(str.encode(str(total))) # return division of two numbers sent by client
  else:
    conn.send(str.encode('Não foi possivel realizar a equação')) # return message in case there is no equation to solve.
    break
conn.close()               # close the connection
