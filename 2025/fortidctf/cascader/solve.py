from Crypto.Util.number import long_to_bytes as ltb, bytes_to_long as btl
import hashlib
from Crypto.Cipher import AES

alice_pub = 81967497404473670873986762408662347640688858544889917659709378751872081150739
bob_pub = 25638634989672271296647305730621408042240305773269414164982933528002524403752

ct = bytes.fromhex('e2f84b71e84c8d696923702ddb1e35993e9108289e2d14ae8f05441ad48d1a67ead74f5f230d39dbfaae5709448c2690237ac6ab88fc26c8f362284d1e8063491d63f7c15cc3b024c62b5069605b73dd2c54fdcb2823c0c235b20e52dc5630c5f3')

SEED = (1 << 256) // 5

p = (1 << 256) - 189


iv = ct[:12]
tag = ct[:-16]
c = ct[12:-16]


alice_f = (alice_pub * pow(SEED, -1, p)) % p
shared = (bob_pub * alice_f) % p

key = hashlib.sha256(ltb(shared)).digest()


cipher = AES.new(key, mode=AES.MODE_GCM, nonce=iv)

print(cipher.decrypt(c))