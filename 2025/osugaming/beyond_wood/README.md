## Solution
The position recovery is straight forward, so I'll not mention it here.     
My idea was supposed that the first pixel of the original flag is a white pixel `(0xff, 0xff, 0xff)`, so the key will be obtained by:

```python
new_pos = transform(0, 0)
xored = output.getpixel(new_pos)
key = [x ^ y for x, y in zip(xored, [0xff, 0xff, 0xff])]
```

## Flag
```
osu{h1_05u_d351gn_t34m}
```