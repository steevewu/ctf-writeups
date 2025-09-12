from pwn import remote, process, context
# context.log_level = 'debug'
from sage.all import *
from Crypto.Util.number import long_to_bytes as ltb, bytes_to_long as btl
import os, sys
sys.path.append(os.path.dirname(__file__))
from acd import ACD

hid = bytes.fromhex('3031300d060960864801650304020105000420')
padding = b'\x00\x01' + b'\xff' * (256 - 32 - len(hid) - 3) + b'\x00' + hid
padding = btl(padding)

dir = os.path.dirname(__file__)
io = process(['python3', dir + '/chall.py'])
def get_sample():
    global io
    io.sendlineafter(b'> ', b'1')
    return int(io.recvline_contains(b'sig = ').strip().decode().split('= ')[1], 16)



e = 11
io.sendlineafter(b'> ', b'2')
flag = int(io.recvline_contains(b'sig = ').strip().decode().split('= ')[1], 16)


xs = [get_sample() for _ in range(32)]

xs = [x**11 - padding * 2**256 for x in xs]

n = ACD.attack(xs, rho=256)[0]


print(ltb(pow(flag, e, n)))