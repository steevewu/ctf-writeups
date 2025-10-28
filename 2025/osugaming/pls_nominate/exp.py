from sage.all import *
import os, sys
from Crypto.Util.number import bytes_to_long, long_to_bytes
sys.path.append(os.path.dirname(__file__))
from output import *


msg = b"hello there can you pls nominate my map https://osu.ppy.sh/beatmapsets/2436259 :steamhappy: i can bribe you with a flag if you do: " + b'X' * flen
flag = b"X" * flen
m = bytes_to_long(msg)
f = bytes_to_long(flag)
index = msg.find(flag)
shift = len(msg) - index - len(flag)
shift *= 8

mm = m - 2**shift * f
c = crt(rs, ns)
x, = PolynomialRing(Zmod(prod(ns)), 'x', implementation='NTL').gens()
poly = (mm + 2**shift * x)**5 - c
poly = poly.monic()

r = poly.small_roots(epsilon=1/25, algorithm='fpLLL:proved', fp='rr')[0]


print(long_to_bytes(r))