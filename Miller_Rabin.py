#Miller_Rabin
import random

# cal (a*b) % c 
def mult_mod(a, b, c):
    return a*b % c

# cal x^n % c
def pow_mod(x, n, c):
    if(n == 1):
        return x % c
    x %= c
    tmp = x
    ret = 1
    while(n):
        if(n&1):
            ret = mult_mod(ret, tmp, c);
        tmp = mult_mod(tmp, tmp, c);
        n >>= 1
    return ret

# n - 1 = x *2^t            a^(n-1) = 1(mod n) check n is prime?
def check (a, n, x, t):
    ret = pow_mod(a, x, n)
    last = ret
    for i in range(0, t) :
        ret = mult_mod(ret, ret, n);
        if (ret == 1 and last != 1 and last != n-1): return True
        last = ret
    if (ret != 1): return True
    return False

def Miller_Rabin(n):
    if(n<2) : return False
    if(n==2) : return True
    if(not(n&1)) : return False
    x = n - 1
    t = 0
    S = 20
    while((x&1)==0):
        x >>= 1
        t += 1
    for i in range(0, S):
        a = random.randint(0, n)
        if (check(a, n, x, t)):
            return False
    return True

while True:
    n = random.randint(2**133, 2**134)
    if (Miller_Rabin(n)):
        p = n;
        break;

while True:
    n = random.randint(2**133, 2**134)
    if (Miller_Rabin(n)):
        q = n;
        break;

print ("p = ", p, '\n', "q = ", q, '\n')
