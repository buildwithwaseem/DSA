def diamond_pyramid(n):
    #============================
    # PART 1 - UPPER HALF OF DIAMOND
    #============================

    for i in range(n):
        for j in range(n - i -1):
            print(' ',end='')
        for k in range(2 * i +1):
            print('*',end='')
        print()

    #============================
    # PART 2 - LOWER HALF OF DIAMOND
    #============================
    for i in range(n):
        for j in range(i):
            print(' ',end='')

        for k in range(2 *(n-i)-1):
            print('*', end='')
        print()

n=5
diamond_pyramid(n)  