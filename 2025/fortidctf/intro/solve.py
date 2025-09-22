import os
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Util.number import inverse
from math import gcd


dir = os.path.dirname(__file__)

n1 = RSA.import_key(open(dir+'/key1.pub', 'rb').read()).n
n2 = RSA.import_key(open(dir+'/key2.pub', 'rb').read()).n

p = gcd(n1, n2)
q1, q2 = n1//p, n2//p
d1, d2 = inverse(65537, (p-1) * (q1-1)), inverse(65537, (p-1) * (q2-1))

c1 = bytes.fromhex(open(dir + '/flag1.enc').read().strip())
c2 = bytes.fromhex(open(dir + '/flag2.enc').read().strip())

key1 = RSA.construct((n1, 65537, d1))
key2 = RSA.construct((n2, 65537, d2))
ct1 = PKCS1_OAEP.new(key1, SHA256)
ct2 = PKCS1_OAEP.new(key2, SHA256)

print(ct1.decrypt(c1))
print(ct2.decrypt(c2))