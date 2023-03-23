# import math
# print("[")
# for i in range(0,257,1):
#     print((1175**i)%3329,end='')
#     print(", ",end='')
# print("]")
import math
def bit_reverse(n):
    reversed_n = 0
    for i in range(7):
        reversed_n = (reversed_n << 1) | (n & 1)
        n >>= 1
    return reversed_n

if __name__ == '__main__' :
    # print("[")
    for i in range(0,128,1):
        r_i=bit_reverse(i)
        # print(r_i)
        print((17**r_i)%3329,end='')
        print(", ",end='')
    # print("]")