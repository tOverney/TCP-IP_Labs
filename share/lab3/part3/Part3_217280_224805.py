from multiprocessing import Process, Pool
import multiprocessing
import os
import socket
import time
import numpy as np

HOST = 'lab3.iew.epfl.ch'
PORT = 5004
DEFAULT_N = 20
MAX_TRIES = 100
MESSAGE = "RESET:{}".format(DEFAULT_N)

######################

def ping_server(af, message=MESSAGE, host=HOST, port=PORT):
    sock = socket.socket(af, socket.SOCK_DGRAM)
    sock.settimeout(1)
    
    sock.sendto(b''+message.encode(), (host,port))
    data = None
    try:
        data, _ = sock.recvfrom(1024)
        return (data.decode(), af)
    except socket.timeout:
        return (data, af)

def run_iteration(pool):
    for i in range(MAX_TRIES):
        results = [pool.apply_async(ping_server,[sock]) for sock in [socket.AF_INET, socket.AF_INET6]]
        data = []
        for result in results:
            (data, af) = result.get()
            if data:
                return (i, af)

#######################

if __name__ == '__main__':
    ack_index = []
    pool = Pool(multiprocessing.cpu_count())

    for _ in range(200):
        i, af = run_iteration(pool)
        print('{} after {} tries'.format(af,i))
        ack_index.append(i)        

    print(ack_index)
    print(np.average(ack_index))
    pool.close()
    pool.join()