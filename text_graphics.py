
rows = 5
cols = 8

for x in range(rows):
    for y in range(cols):
        print("*", end='')
    print()


print('\n')


rows = 6
cols = 8

for x in range(rows):
    if x==0 or x==rows-1:
        for y in range(cols):
            print("#", end='')
    if x>=1 and x<=rows-2:
        for y in range(cols):
            if y==0 or y==cols-1:
                print("#", end='')
            if y>=1 and y<=cols-2:
                print(" ", end='')
    print("")


print('\n')


def print_square(N):
    list(map(print, ['*' * N] * N))
print_square(6)


print('\n')


def circle(r):
    n = 2 * r
    c_x = r
    c_y = r
    for x in range(-r, r + 1):
        for y in range(-r, r + 1):
            if x ** 2 + y ** 2 < r ** 2:
                print('# ', end='')
            else:
                print('. ', end='')
        print()
 
circle(5)


print('\n')


def circle(d, t):
    r = 2 * t + d + 1
    n = 2 * r
    for x in range(-r, r + 1):
        for y in range(-r, r + 1):
            z = x ** 2 + y ** 2
            if z < t ** 2 or (t + d) ** 2 <= z < (2 * t + d) ** 2:
                print('# ', end='')
            else:
                print('. ', end='')
        print()
 
 
circle(4, 2)


print('\n')


result_str=""    
for row in range(0,7):    
    for column in range(0,7):     
        if (column == 3 or (row == 0 and column > 0 and column <6)):  
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str)


print("\n")


def printT(n):
    for i in range(0, n):
        for j in range(0, n):
            if (i == 0):
                print("*", end="")
            elif (j == n // 2 ):
                print("*", end="")
            else:
                print(end=" ")
        print()

printT(7)


def bigT(n):
    print("#" * n, (n-1) * "\n#")
    

print("\n")


def pyramid(n):
    k = 0
    for i in range(1, n+1):
        for space in range(1, (n-i)+1):
            print(end="  ")
        while k!=(2 * i - 1):
            print("# ", end="")
            k += 1 
        k = 0
        print()
        
pyramid(7)


print("\n")


def arrow(n):
    for i in range(n):
        for j in range(n):
            if (j-i==(n - 1) // 2 or i+j==3 * n // 2 - 1 or i==(n - 1) // 2):
                print("*", end="")
            else:
                print(".", end="")
        print()

arrow(11)


print('\n')


def chessboard(n):
    for i in range(n):
        for j in range(n):
            c = "#" if ((i+j) % 2 == 0) else "."
            print(c, end="")
        print()

chessboard(11)


print('\n')


def cross(n):    
    for i in range(3*n):
        for j in range(3*n):
            if i >= n and i <= n+n-1 or j >= n and j <= n+n-1:
                print("#", end="")
            else:
                print(".", end="")
        print()

cross(2)
print()
cross(4)


print('\n')


def make_fancy(text, n):
    cnt = 0
    for cr in text:
        for i in range(cnt):
            print(end=' ')
        for i in range(n):
            print(cr, end=' ')
        print()
        cnt += 1
        
make_fancy("PTAKOPYSK", 5)


print('\n')


print('Stars stairs:')

def stars(n):
    for i in range(n):
        print("*", end='')
        if i % 5 == 4:
            print("|", end="")

    print()

stars(7)
stars(15)


print('\n')


print('Chessboard (not complited)')

def big_chessboard(n, m):
    for i in range(n):
        for j in range(n):
            c = "#"*m if ((i+j) % 2 == 0) else "."*m
            print(c, end="")
        print()

big_chessboard(5, 3)

#    print("#", end="")
#    print(".", end="")


print()


print('Big Chessboard:')

def Big_Chessboard(n, m):
    for i in range(n):
        for j in range(m):
            for j in range(n):
                c = "#"*m if ((i+j) % 2 == 0) else "."*m
                print(c, end="")
            print()

Big_Chessboard(6, 2)
print()
Big_Chessboard(5, 3)


print('\n')


print('Chessboard:')

def chessboard(n):
    for i in range(n):
        line(n, i % 2)

def line(n, parity):
    for j in range(n):
        if (j % 2 == parity): print("#", end="")
        else: print(".", end="")
    print()

chessboard(10)


print('\n')


side = 5

print("Square Star Pattern") 

for i in range(side):
    for i in range(side):
        print('*', end = '  ')
    print()


print('\n')


print("Square Star Pattern")

side = 5
i = 0

while(i < side):
    j = 0
    while(j < side):      
        j = j + 1
        print('*', end = '  ')
    i = i + 1
    print('')


print('\n')


def triangle(c, n):
    for i in range(n, 0, -1):
        print(c * i)

triangle("X", 5)


print('\n')


