def bit_reverse(n):
    reversed_n = 0
    for i in range(7):
        reversed_n = (reversed_n << 1) | (n & 1)
        n >>= 1
    return reversed_n


if __name__ == '__main__' :
    f = open("root_256_r.txt","r")
    roots = f.read().split(', ')
    f1 = open("even_coef_r.txt","r")
    even_coef = f1.read().split(', ')
    f2 = open("odd_coef_r.txt","r")
    odd_coef = f2.read().split(', ')

    ################    INTT     ################

    ################
    ##    EVEN    ##
    ################
    print("The original even coefficients are: ")
    for i in range(0,128,1):
        coef_even = 0
        # reverse_i = bit_reverse(i)
        for j in range(0,128,1):
            reverse_j = bit_reverse(j)
            mul = ((2*reverse_j+1)*i)%128
            coef_even += int(even_coef[j])*int(roots[mul])

        ans=int(coef_even/128)
        print(ans%3329,end='')
        print(", ",end='')

    print("End of even coefficient")
    ################
    ##    ODD     ##
    ################
    # print("The original odd coefficients are: ")
    # for i in range(0,128,1):
    #     coef_odd = 0
    #     reverse_i = bit_reverse(i)
    #     for j in range(0,128,1):
    #         mul = ((2*reverse_i+1)*j)%128
    #         coef_odd += int(polys[j*2+1])*int(roots[mul])
    #     print(coef_odd%3329,end='')
    #     print(", ",end='')

    # print("End of odd coefficient")

    f.close()
    f1.close()