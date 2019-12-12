#!/usr/bin/python

import socket
import sys
import time
import threading
import numpy as np
import csv

with open("graph" + sys.argv[2] + ".csv", mode='w') as csv_file:
    fieldnames = ['bandwidth', 'time', 'sequence']
    graph_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    graph_writer.writeheader()

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening

server_address = (sys.argv[1], int(sys.argv[2]))
#print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

total_byte_sent = np.int64(0)
def send_data(msg):
    byte_sent = 0
    while(1):
        message = bytes(65533)
        global server_address
        byte_sent = sock.sendto(message, server_address)
        if byte_sent > 0:
            global total_byte_sent
            total_byte_sent = total_byte_sent + byte_sent

total_bytes_sent_second_ago = np.int64(0)
def log_speed(msg):
    log_index = 0
    sequence = 0
    while(1):
        time.sleep(1)
        global total_byte_sent
        global total_bytes_sent_second_ago
        bandwidth = (total_byte_sent - total_bytes_sent_second_ago)/125000
        print("Bandwidth: " + str(round(bandwidth,2)) + "Mbits/s")
        sequence = sequence + 1
        with open("graph" + sys.argv[2] + ".csv", mode='a') as csv_file:
            graph_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            graph_writer.writerow({'bandwidth': bandwidth, 'time': str(time.time()), 'sequence' : str(sequence)})
        total_bytes_sent_second_ago = total_byte_sent

try:
    x = threading.Thread(target=send_data, args=(0,), name="Thread-01")
    y = threading.Thread(target=log_speed, args=(0,), name="Thread-02")
    x.start()
    y.start()

finally:
    print("success")
