import math
print("[")
for i in range(0,257,1):
    print((1175**i)%3329,end='')
    print(", ",end='')
print("]")