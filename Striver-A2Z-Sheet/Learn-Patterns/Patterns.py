''' 1.
*****
*****
*****
*****
*****
'''

def patterns(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()

n =5
patterns(n)

#------------------------------------------------------------

'''2. Right Triangle
*
**
***
****
*****
'''
def right_angle_triangle(n):
    for i in range(n):
        for j in range(i+1):
            print('*', end='')
        print()

n = 5
right_angle_triangle(n)

#------------------------------------------------------------

'''3. number triangle
1
12
123
1234
12345
'''
def number_triangle(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end="")
        print()

n = 5
number_triangle(n)

#------------------------------------------------------------

'''4. 
1
22
333
4444
55555
'''
def same_num_triangle(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(i, end="")
        print()

n =5
same_num_triangle(n)

'''5. Inverted Triangle
*****
****
***
**
*
'''
def inverted_triangle(n):
    for i in range(n):
        for j in range(n-i):
            print('*', end='')

        print()

n =5
inverted_triangle(n)

'''6.
12345
1234
123
12
1
'''

def inverted_number_triangle(n):
    for i in range(n):
        for j in range(1, n-i +1):
            print(j, end='')
        print()

n=5
inverted_number_triangle(n)



'''7. 
    *
   ***
  *****
 *******
*********
'''

def star_pyramid(n):
    for i in range(n):
        for j in range(n -i -1):
            print(' ', end='')
        
        for k in range(2 * i +1):
            print('*', end='')
        print()

n = 5
star_pyramid(n)

'''8.
*********
*******
*****
***
*
'''

def inverted_pyramid(n):
    for i in range(n):
        for j in range(n):
            print(' ', end='')
        for k in range(2 * (n-i) - 1):
            print('*', end='')
        print()

n=5
inverted_pyramid(n)

'''9.
    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
'''
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
            
        

            









