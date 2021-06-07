import socket 
import time
import threading

k_recv_s=socket.socket()
k_recv_s.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1) #this is done so that we can reuse a port, otherwise everytime we have 
#to kill service because till some time port is remains active

s_recv_s=socket.socket()
s_recv_s.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)

k_send_s=socket.socket()
k_send_s.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)

s_send_s=socket.socket()
s_send_s.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)

k_recv_port=2024 #recive from kalyani
s_recv_port=2025 #recive from sudhanshu
k_send_port=2026 #send to kalyani
s_send_port=2027 #send to sudhanshu
ip=""
k_recv_s.bind((ip, k_recv_port))
s_recv_s.bind((ip, s_recv_port))
k_send_s.bind((ip, k_send_port))
s_send_s.bind((ip, s_send_port))

k_recv_s.listen()
s_recv_s.listen()
k_send_s.listen()
s_send_s.listen()

k_recv_session, k_recv_addr = k_recv_s.accept()
s_recv_session, s_recv_addr = s_recv_s.accept()
k_send_session, k_send_addr = k_send_s.accept()
s_send_session, s_send_addr = s_send_s.accept()

#above we have created total 4 socket 1) it will recive image in bytes from person2
#2)it will send those bytes recived by person2 to the person1
#3)it will recive image in bytes from person1
#2)it will send those bytes recived by person1 to the person2
def k_recv(): #it will recive from kalyani and send to sudhanshu
    while True:
        data=k_recv_session.recv(10000000)
        time.sleep(2)
        s_send_session.send(data)

def s_recv(): #it will recive from sudhanshu and send to kalyani
    while True:
        data=s_recv_session.recv(10000000)
        time.sleep(2)
        k_send_session.send(data)
#used threading so that above both function will run parellely
k1_recv=threading.Thread(target=k_recv)
s1_recv=threading.Thread(target=s_recv)
k1_recv.start()
s1_recv.start()