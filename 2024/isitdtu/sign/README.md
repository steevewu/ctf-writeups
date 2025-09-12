## Solution
Since $flag$ is encrypted using private exponent $d$, and public exponent $e=11$, our mission is recovering the modolo $n$.

As in [Evaluation of Security Level of Cryptography:
RSA Signature Schemes (PKCS#1 v1.5, ANSI X9.31, ISO 9796)](https://www.cryptrec.go.jp/exreport/cryptrec-ex-1014-2002.pdf) - Section 4, the signature scheme is operated over an octet string $M$ in the form:

$$
00 || 01 || PS || 00 || HID || h
$$
where:
1. $h$: hash digest of original message $m$.
2. $HID$: hash identifier of hash algorithm (the HID can be [found here](https://www.ibm.com/docs/en/zos/3.1.0?topic=cryptography-pkcs-1-formats)).
3. $PS$: a string of $0xff$ octets, $||PS|| = k - ||h|| - ||HID|| - 3$, for $k$ is octet length of modulo $n$. (note: $||PS|| \geq 8$).

As for each message, only $h$ is variant, then $M$ can be written as follow:

$$
M = (01||PS||00||HID) * 2^{q} + h = padding + h
$$
where $q$ is bit-length of $h$.     
$M$ is then encrypted using private key $(d, n)$, as follow:

$$
sig \equiv M^d \mod{n}
$$

or, precisely,

$$
sig \equiv M^d \equiv (padding + h)^d \mod{n}
$$

Then, in validation stage, $sig$ is extracted as:

$$
sig^e \equiv M^{d*e} \equiv (padding + h)^{d*e} \equiv padding + h \mod{n}
$$

then, we can easily obtain that

$$
sig^e - padding = k*n + h
$$
This fact leads to a solvable problem, i.e the [approximate common divisor](https://martinralbrecht.wordpress.com/2020/03/21/the-approximate-gcd-problem/) which is distinguished as:

$$
x_i = p * q_i + r_i
$$


As server accepts unlimited access to generate random message's signature, we can create a sample of $x_i$ and using ACD to find $n$.
## Flag
```

```