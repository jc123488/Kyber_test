def bit_reverse(n):
    reversed_n = 0
    for i in range(7):
        reversed_n = (reversed_n << 1) | (n & 1)
        n >>= 1
    return reversed_n


if __name__ == '__main__' :
    f=open("root_128.txt","r")
    roots = f.read().split(', ')
    f1=open("poly_256.txt","r")
    polys = f1.read().split(', ')

    ################    NTT     ################

    ################
    ##    EVEN    ##
    ################

    # print("The 7th stage even coefficients are: ")
    
    coef=[0]*256

    for i in range(0,256,1):
        coef[i] = int(polys[i])

    for i in range(0,128,1):
        coef_even = 0
        reverse_i = bit_reverse(i)
        for j in range(0,128,1):
            mul = ((2*reverse_i+1)*j)%256
            coef_even += int(polys[j*2])*int(roots[mul])
        print(coef_even%3329,end='')
        print(", ",end='')
        # coef[i*2]=coef_even%3329
    # len = 128
    # start = 0
    # k = 1
    # while len >= 2:
    #     while start < 256:
    #         k = k+1
    #         zeta = int(roots[1])
    #         j = start
    #         range = start+len
    #         while j < range:
    #             t = zeta * coef[j+len]
    #             coef[j+len] = coef[j] - t
    #             coef[j] = coef[j] + t
    #             j=j+1
    #     len = len/2

    print("\n")
    print("End of even coefficient")
    print("\n")
    
    ################
    ##    ODD     ##
    ################

    print("The 7th stage odd coefficients are: ")
    for i in range(0,128,1):
        coef_odd = 0
        reverse_i = bit_reverse(i)
        for j in range(0,128,1):
            mul = ((2*reverse_i+1)*j)%256
            coef_odd += int(polys[j*2+1])*int(roots[mul])
        # print(coef_odd%3329,end='')
        
        # print(", ",end='')
        coef[i*2+1]=coef_odd%3329

    # print("End of odd coefficient")

    for i in range(0,256,1):
        # print("i= ",i,"coef= ",coef[i])
        print(coef[i]%3329,end='')
        print(", ",end='')

    f.close()
    f1.close()