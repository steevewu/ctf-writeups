from pwn import remote, process, context
import os
from Crypto.Util.number import *
from sage.all import *



context.log_level = 'debug'
dir = os.path.dirname(__file__)


p = (1 << 255) - 19


# conn = process(['python3', dir + '/chall.py'])
conn = remote('ssss.challs.sekai.team', 1337)

conn.recvline(); conn.recvline()

y_pos, y_neg = list(), list()
for x in range(1, 4):
    conn.sendline(str(x).encode())
    y_pos.append(int(conn.recvline().strip().decode()) % p)
    
    conn.sendline(str(p - x).encode())
    y_neg.append(int(conn.recvline().strip().decode()) % p)


inv_2 = pow(2, -1, p)

alphas, betas = list(), list()
for i in range(3):
    alpha = ((y_pos[i] + y_neg[i]) * inv_2) % p
    beta = ((y_pos[i] - y_neg[i]) * inv_2) % p
    alphas.append(alpha)
    betas.append(beta)

F = GF(p)
B = vector(F, alphas)
mt = []

for i, x in enumerate(range(1, 4)):
    mt.append([betas[i] * x, sum([x**e for e in range(2, 15, 2)]), 1])

A = matrix(F, mt)

sec = A.solve_right(B)[-1]
for _ in range(8):
    conn.sendline(str(1337).encode()); conn.recvline()

conn.sendlineafter(b'secret? ', str(sec).encode())
conn.interactive()    