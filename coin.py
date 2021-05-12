import socket

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Como é importante chegar ao destino e não tem muitos dados, a melhor opção é  o tcp.

ip = ''
porta = 5000
origem = (ip, porta)
tcp.bind(origem)
tcp.listen(1)
tcp_dados, cliente = tcp.accept

ip_serv = '127.0.0.1'
porta_serv = 5000
dest = (ip_serv, porta_serv)
tcp.connect(dest)

msg = input()
tam = (len(msg)).to_bytes(6, 'big')
tcp.send(tam + msg.encode())
tam_resp = int.from_bytes(tcp.recv(16), 'big')
resp = tcp.recv(tam_resp)
print('Resposta', resp.decode())
tcp.close()
input('aperte enter para encerrar')

