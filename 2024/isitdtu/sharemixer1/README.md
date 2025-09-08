## Solution
Since server accpet $256$ element each query, we can determine which output belongs to a specific input by counting their appearances. However, as $32$ is the rank of coefficient matrix, $256$ will not be clear enough for mapping obtained result.      
We then have to separate payload into groups of same appearances, then for each of their permutation, solving the linear equation system below over $GF(p)$.

$$
A \times X \equiv B
$$

For each result $X$, check if flag lies in vector $X$.

## Flag
```
ISITDTU{Mix1_a5850c98ad583157f0}
```