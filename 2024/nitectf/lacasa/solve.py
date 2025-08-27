from pwn import remote, process, context
context.log_level = 'debug'
from sage.all import *
from Crypto.Util.number import long_to_bytes as ltb, bytes_to_long as btl
import os, random

dir = os.path.dirname(__file__)
io = process(['python3', dir + '/chall.py'])



io.sendlineafter(b"option: ", b"1")
io.sendlineafter(b"message: ", b"Bob33")
hash = io.recvline().decode().strip().split(": ")[1]
hash = base64.b64decode(hash)

io.sendlineafter(b"option: ", b"2")
io.sendlineafter(b"name: ", b"Bob33")
io.sendlineafter(b"HMAC: ", hash)
password = io.recvlinesS(3)[-1]

io.sendlineafter(b"option: ", b"3")
io.sendlineafter(b"Password: ", password.encode())


io.interactive()