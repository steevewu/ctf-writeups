from sage.all import ZZ, matrix

class ACD:
    @staticmethod
    def __symmetric_mod(x, m):
        return int((x + m + m // 2) % m) - int(m // 2)
               
    @staticmethod
    def attack(xs: tuple[int,...], rho: int):
        assert len(xs) >= 2, 'Not enough samples to find'
        
        R = 2 ** rho

        B = matrix(ZZ, len(xs), len(xs) + 1)
        for i, xi in enumerate(xs):
            B[i, 0] = xi
            B[i, i + 1] = R

        B = B.LLL()

        K = B.submatrix(row=0, col=1, nrows=len(xs) - 1, ncols=len(xs)).right_kernel()
        q = K.an_element()
        r0 = ACD.__symmetric_mod(xs[0], q[0])
        p = abs((xs[0] - r0) // q[0])
        r = [ACD.__symmetric_mod(xi, p) for xi in xs]
        if all(-R < ri < R for ri in r):
            return int(p), r