## Solution
Since server accepts only $k-1$ queires, we cannot directly reconstruct the [Lagrange polynomial](https://en.wikipedia.org/wiki/Lagrange_polynomial) to recover flag.   

However, we can leverage the fact that,     
$$
\frac{f(x) + f(-x)}{2} = \sum_{i=0, \ even}^{14}c_ix^i = \alpha
$$


similarly, we can easily obtain the odd part by,

$$
\frac{f(x) - f(-x)}{2} = \sum_{i=1, \ odd}^{13}c_ix^i = \beta
$$

By implementing $\alpha$, we receive,

$$
\begin{align*}
\alpha &= \sum_{i=0, \ even}^{14}c_ix^i \\\\
&= c_0 + \sum_{i=2, \ even}^{14}c_ix^i \\\\\
&= c_0 + \sum_{i=2, \ even}^{14}(a * c_{i-1} + b) * x^i \\\\
&= c_0 + \sum_{i=2, \ even}^{14}(a * c_{i-1}) * x^i + b * \sum_{i=2, \ even}^{14}x^i \\\\
&=c_0 + a * x * \sum_{i=1, \ odd}^{13}c_i x^i + b * \sum_{i=2, \ even}^{14} x^i \\\\
&= a * x * \beta + b * \sum_{i=2, \ even}^{14} x^i + c_0
\end{align*}
$$

Gathering 3 pairs of $\alpha$ and $\beta$ and recover $a$, $b$, $c_0$ by solving a linear equation system.

## Flag
```
osu{0n3_hundr3d_p3rc3nt_4ccur4cy!}
```