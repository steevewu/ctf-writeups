## Solution
The construction formula of $n$ can be written as $n = p * q * (p + 1) * (p - 1) * (q + 1) * (q - 1)$, since $p$ and $q$ are both odd number, then $n$ must be an even. The [Chinese remainder theorem](https://en.wikipedia.org/wiki/Chinese_remainder_theorem) said that we can find a solution for $x$ for a system of congruence equations where $n_i$ must be pairwise coprime. In this case, $n$ is even, so that $n_i$ are not coprime at all. Thus, we need to slightly manipulate this property to make CRT plays a role.  
The following image is an illustration:

<div align="center">
<img src='https://64.media.tumblr.com/a551b8ba8a01d509627957e1c3a4ca84/fb3ee2941e0bce51-a2/s1280x1920/038a77694f48d86f8985daf1212e60c975bb5225.pnj' width=720>
</div>

Next step, cuz $e$ is randomly pick in range $[p*q, (p*q)^2]$, we need to gacha til $e$ is coprime with $p - 1$, in order to make [Euler's theorem](https://en.wikipedia.org/wiki/Euler%27s_theorem) make sense. By now, we just need to find actual remainders of $x \mod{p}$ by using RSA decryption formula:

$$
r \equiv c^d \mod{p}
$$

where $d \equiv e^{-1} \mod(p-1)$.

Finally, use CRT to solve congruence system and recover $m_1, m_2, m_3$, then find $flag_1, flag_2, flag_3$ by solving the equation:

$$
x^3 - m_2*x^2 + m_3*x - m_1 = 0
$$

Our $flag$ is the concatenation of $x1$, $x2$, and $x3$.

## Flag
```
W1{wi3rd_ch41!En9e_n33d_4_WlErD_s0O!luti0n_6f339749663eeb3508c3b00c15872e41}
```