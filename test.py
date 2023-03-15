import math

# 定義模數和原根
MOD = 3329
PRIMITIVE_ROOT = 17

# 求解模數下的乘法反元素
def mod_inverse(a, mod):
    a %= mod
    for x in range(1, mod):
        if (a * x) % mod == 1:
            return x
    return None

# NTT
def ntt(f, inverse=False):
    n = len(f)
    if n == 1:
        return f
    # 求解n次單位根
    w_n = pow(PRIMITIVE_ROOT, (MOD - 1) // n, MOD)
    if inverse:
        w_n = mod_inverse(w_n, MOD)
    # 將f分為奇偶兩部分
    f_even = [f[i] for i in range(0, n, 2)]
    f_odd = [f[i] for i in range(1, n, 2)]
    # 遞迴求解f_even和f_odd的n次NTT
    y_even = ntt(f_even, inverse)
    y_odd = ntt(f_odd, inverse)
    # 合併y_even和y_odd
    y = [0] * n
    w = 1
    for i in range(n // 2):
        y[i] = (y_even[i] + w * y_odd[i]) % MOD
        y[i + n // 2] = (y_even[i] - w * y_odd[i]) % MOD
        if inverse:
            y[i] = (y[i] * mod_inverse(2, MOD)) % MOD
            y[i + n // 2] = (y[i + n // 2] * mod_inverse(2, MOD)) % MOD
        w = (w * w_n) % MOD
    return y

# INTT
def intt(f):
    n = len(f)
    y = ntt(f, inverse=True)
    for i in range(n):
        y[i] = (y[i] * mod_inverse(n, MOD)) % MOD
    return y

# 範例
f = [1, 2, 3, 4, 5, 6, 7, 8] # 要進行NTT的序列
g = ntt(f) # 對序列進行NTT
f_recovered = intt(g) # 對NTT結果進行INTT，還原原序列
print(f)
print(g)
print(f_recovered)
