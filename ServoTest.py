import RPi.GPIO as GPIO
import time
import socket

TCP_IP = "192.168.24.239"
TCP_PORT = 9576

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(s)

s.connect((TCP_IP, TCP_PORT)) 

data = s.recv(1024)

print(data)
