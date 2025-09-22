## Solution
As described in [Shared Key Recovery Attack on Cascader Key Exchange Protocol](https://eprint.iacr.org/2025/1418.pdf), when $SEED$ is set to $\frac{2^{256}}{5}$, then $F(SEED, e) = SEED \cdot P(e)$, where:

$$
P = \prod_{j  \in \mathcal{I}(e)}(3^j \cdot 2^{\frac{j(j-1)}{2}}) \pmod{p}
$$

with $\mathcal{I}(e)$ is defined as follow:

$$
\mathcal{I}(e) = \{j \in 1, 2, 3, ..., 256 | e_{j-1} = 1 \}
$$

Lemme re-write the public-key generation process of Alice (let's call it $A$),

$$
A = F(SEED, alice\_private) = SEED \cdot P(alice\_private) \pmod{p}
$$

so that, 
$$
P(alice\_private) = SEED^{-1} \cdot A \pmod{p}
$$


Then the shared key could be computed as:

$$
S = B * P(alice\_private) \pmod{p}
$$


## Flag
```
FortID{St0p_B31n6_4_H1ps73r_4nd_5t1ck_70_Th3_G00d_0ld_D1ff1e_H3l1man}
```