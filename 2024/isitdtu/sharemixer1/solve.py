from pwn import remote, process, context
context.log_level = 'debug'
from sage.all import *
from Crypto.Util.number import long_to_bytes as ltb, bytes_to_long as btl
import os, re, itertools, collections, tqdm




dir = os.path.dirname(__file__)
io = process(['python3', dir + '/chall.py'])
    
c1 = list(range(1, 5))
c2 = sum([[n] * 2 for n in range(5, 9)], [])
c3 = sum([[n] * 3 for n in range(9, 11)], [])
c4 = sum([[n] * 4 for n in range(11, 13)] , [])
c5 = sum([[n] * (n - 8) for n in range(13, 33)] , [])
assert len(c1 + c2 + c3 + c4) <= 256

p = int(io.recvline_contains(b'p', keepends=False).decode().split('= ')[1])
F = GF(p)


io.sendlineafter(b'queries: ', ' '.join(map(str, c1 + c2 + c3 + c4 + c5)).encode())


shares = eval(io.recvline_contains(b'shares', keepends=False).decode().split('= ')[1])

lz = collections.Counter(shares)
lz = {k: v for k, v in sorted(lz.items(), key=lambda item: item[1])}.keys()
B = vector(F, lz)




subs = [sorted(list(set(c))) for c in [c1, c2, c3, c4]]
perms = [list(itertools.permutations(sub)) for sub in subs]
combs = list(itertools.product(*perms))

fixed = list(range(13, 33))

for com in tqdm.tqdm(combs):
    shuff = sum([list(x) for x in com], [])
    mat = [[pow(x, i, p) for i in range(32)] for x in shuff + fixed]
    
    assert len(mat) == 32
    
    A = Matrix(F, mat)
    X = ~A * B
    for f in X:
        if re.match(b'ISITDTU{.*}', ltb(int(f))):
            print(ltb(int(f)))
            exit()


