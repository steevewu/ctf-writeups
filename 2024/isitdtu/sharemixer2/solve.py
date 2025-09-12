from sage.all import *
from pwn import *
from Crypto.Util.number import long_to_bytes as ltb
import random, re

context.log_level = 'debug'

dir = os.path.dirname(__file__)



while True:
    io = process(['python3', dir + '/chall.py'])
    p = int(io.recvline().strip().decode().split('= ')[1])

    if (p - 1) % 32 != 0:
        io.close()
        continue
    
    g = int(GF(p).multiplicative_generator())
    g = pow(g, (p-1)//32, p)

    xs = [pow(g, i, p) for i in range(32)]

    payload = ' '.join(map(str, xs)).encode()
    
    io.sendlineafter(b'queries: ', payload)
    
    shares = eval(io.recvline().strip().decode().split('= ')[1])

    flag = sum(shares) * pow(32, -1, p) % p
    
    if re.match(b'ISITDTU{.*}', ltb(int(flag))):
        print(ltb(int(flag)))
        exit()
    