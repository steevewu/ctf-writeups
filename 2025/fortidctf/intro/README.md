## Solution
I've asked the organisers if the flag was encrypted using the public key, and they said that "_not every RSA is textbook RSA_".     
So, it's highly recommend to _guess_ the encryption process that was taken. I finally found out that the [PKCS1 OAEP padding](https://en.wikipedia.org/wiki/Optimal_asymmetric_encryption_padding) was used with `SHA256` hasing function.

## Flag
```
FortID{4nd_1_Sa1d_Wh47_Ab07_4_C0mm0n_Pr1m3_F4ct0r?}
```