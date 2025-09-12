## Solution
In this challenge, the limitation of payload's length is reduced to $32$, which is equal to the degree of our polynomial. Then, bruteforce becomes infeasible, cuz the volume of permutations is $32!$. We have to look for an alternative solution.       

The fact that if $g$ is a $k$-th root of unity modulo $p$, then $g$ has the following property:

$$
g^k \equiv 1 \mod{p}
$$

Additionally, if $(g-1)$ is not a [zero divisor](https://en.wikipedia.org/wiki/Zero_divisor), then $\sum_{i=0}^{k-1} \equiv 0 \mod{p}$, i.e:

$$
(x-1) \sum_{i=0}^{k-1} \equiv x^k - 1 \equiv 0 \mod{p}
$$

Assume that $flag$, after shuffling, be the first entry of our coefficient vector. The challenge can be written as follow:


<div align='center'>
<img src="https://64.media.tumblr.com/c7a3ad9b1b133497e7a080804bed4ae5/468f8f5dfb118ee6-80/s1280x1920/ca91f191519c43f6261d61d13fcbe2b7a6e64d75.pnj" alt="lagrida-latex-editor" border="0">
</div>

By computing the summation of result vector, we have,

$$
sum = 32 * flag + \sum_{i=1}^{31}[c_i * (1 + \sum_{j=1}^{31}g_i^j)]
$$

If we choose a $g$ as a $32$-nd root of unity modulo $p$, then the massive of summation sastisfies:

$$
\sum_{i=1}^{31}[c_i * (1 + \sum_{j=1}^{31}g_i^j)] \equiv 0 \mod{p}
$$

So that, we can recover $flag$ by the formula:

$$
flag \equiv sum * 32^{-1} \mod{p}
$$
## Flag
```
ISITDTU{M1x_4941n!_73360d0e5fb4}  
```