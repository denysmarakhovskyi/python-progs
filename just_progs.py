print("odd and even nums")

def odd_even(n):
    for i in range(1, n+1):
        if i % 2 == 1:
            print(i, end=" ")
    print("\n",  end=" ")
    for i in range(1, n+1):
        if i % 2 == 0:
            print(i, end=" ")

odd_even(22)


print("\n")


print("even numbers")

def even_numbers(n):
    for i in range(2, n*2+1):
        if i % 2 == 0:
            print(i)

even_numbers(5)
print()
even_numbers(10)
print()
even_numbers(22)


print("\n")


print('Tickets price:')

def print_ticket(age):
    if age <= 5:
        print("Cena:", 0)
    elif age <= 17:
        print("Cena:", 50)
    elif age >= 70:
        print("Cena:", 50)
    else:
        print("Cena:", 100)

print_ticket(20)
print_ticket(15)
print_ticket(5)
print_ticket(75)


print('\n')


print('At least one number is divisible by 7:')

def can_visit(x, y, z):
    if x%7 == 0 or y%7 == 0 or z%7 == 0:
        return True
    else:
        return False

print(can_visit(5, 6, 7))
print(can_visit(5, 7, 6))
print(can_visit(15, 16, 17))
print(can_visit(30, 40, 50))
print(can_visit(35, 49, 70))


print('\n')


print('Horseshoes count:')

# ujde to ale...
def check1(p, k):
    if p / k == 4:
        print("OK")
    elif p / k > 4:
        print("Prebyva:", p % 4)
    else:
        print("Chybi:", 4 * k - p)

check1(10, 2)
check1(12, 3)
check1(20, 6)
check1(13, 3)
check1(17, 4)
check1(40, 5)
check1(33, 8)

print("----------------------------------")

# je to mnohem lepe reseni
def check(p, k):
    if p > 4 * k:
        print("Prebyva:", p - 4 * k)
    elif p < 4 * k:
        print("Chybi:", 4 * k - p)
    else:
        print("OK")

check(10, 2)
check(12, 3)
check(20, 6)
check(13, 3)
check(17, 4)
check(40, 5)
check(33, 7)

print("----------------------------------")

def check_eng(p, k):
    if p / k == 4:
        print("OK")
    elif p / k > 4:
        print("Remaining:", p % 4)
    else:
        print("Missing:", 4 * k - p)

check_eng(10, 2)
check_eng(12, 3)
check_eng(20, 6)
check_eng(13, 3)
check_eng(17, 4)

print("----------------------------------")

def check_horseshoes(shoes, horses):
    if shoes > 4*horses:
        print("Remaining:", shoes - 4 * horses)
    elif shoes == 4*horses:
        print("OK")
    else:
        print("Missing:", 4 * horses - shoes)

check_horseshoes(10, 2)
check_horseshoes(12, 3)
check_horseshoes(20, 6)
check_horseshoes(13, 3)
check_horseshoes(17, 4)
check_horseshoes(40, 5)


print('\n')


print('rock, scissors, paper / kamen, nuzky, papir:')

def decide(symbol1, symbol2):
    if symbol1 == "K" and symbol2 == "N":
        print(symbol1)
    elif symbol1 == "P" and symbol2 == "K":
        print(symbol1)
    elif symbol1 == "N" and symbol2 == "P":
        print(symbol1)
    elif symbol1 == "N" and symbol2 == "K":
        print(symbol2)
    elif symbol1 == "K" and symbol2 == "P":
        print(symbol2)
    elif symbol1 == "P" and symbol2 == "N":
        print(symbol2)
    else: 
        print("Remiza")

decide("K", "N")
decide("P", "K")
decide("P", "P")
decide("K", "P")
decide("N", "K")


print("\n")


print('Reverse nums:')

def reverse_numbers(n):
    for i in range(n, 0, -1):
        print(i)

reverse_numbers(33)
print()
reverse_numbers(14)


print("\n")


print('Nums comparing:')

def size_info(n, k):
    for i in range(1, n+1):
        if i < k:
            print(i, "<", k)
        elif i == k:
            print(i, "=", k)
        else:
            print(i, ">", k)

size_info(5, 3)
print()
size_info(11, 7)


print("\n")


print('Factorial:')

def factorial(n):
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial * i
    #print (factorial)
    return factorial

print(factorial(5))
print(factorial(3))
print(factorial(4))
print(factorial(10))


print("\n")


print('Exept nums ending by 5:')

def alergy_list(a, b):
    for i in range(a, b+1):
        if not i % 5 and i % 10:
            continue
        print(i, end=" ")
    print()

alergy_list(3, 27)
alergy_list(41, 48)
alergy_list(1, 7)


print("\n")


print('Printing "*" instead of number:')

def numbers_around(n, k):
    for i in range((n-k),(n+k+1)):
        if i == n:
            print("*", end = " ")
        else:
            print(i, end=' ')
    print()

numbers_around(27, 2)
numbers_around(15, 3)
numbers_around(8, 6)
numbers_around(38, 5)


print("\n")


print('Tax counter:')

def compute_tax(money_list):
    tax = 0
    for money in money_list:
        if money >= 200:
            tax += 20
        elif money >= 100:
            tax += 10
        else:
            tax += 0
        money += tax
    return tax


print(compute_tax([50, 20, 80]))
print(compute_tax([50, 120, 80, 480]))
print(compute_tax([250, 120, 170, 480, 30, 1000]))
print(compute_tax([250, 120, 70, 4080, 30, 120, 600, 78]))

print()

# better one
def compute_tax(money_list):
    tax = 0
    for money in money_list:
        if money >= 100 and money < 200:
            tax += 10
        elif money >= 200:
            tax += 20
        else:
            tax += 0
        money -= tax
    return tax


print(compute_tax([50, 20, 80]))
print(compute_tax([50, 120, 80, 480]))
print(compute_tax([250, 120, 170, 480, 30, 1000]))
print(compute_tax([250, 120, 70, 4080, 30, 120, 600, 78]))


print("\n")


print('Multiples sum:')

def multiples_sum(n):
    res = sum(x for x in range(n) if x % 7 == 0)
    print(res)

multiples_sum(1000)


print("\n")


print('Fibonacci nums:')

def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        print(a)
        a, b = b, a+b

fibonacci(14)


print("\n")


print('Odd fibonacci:')

def odd_fibonacci(n):
    n = (3 * n + 1) // 2
    a = -1
    b = 1
    c = 0
    for i in range(1, n + 1):
        c = a + b
        a = b
        b = c
    return c

# Driver Code
print(odd_fibonacci(4))


print()


print('Function which returns nth even fibonacci number:')

def even_fib(n):
    if (n < 1):
        return n
    if (n == 1):
        return 2

    # calculation of
    # Fn = 4*(Fn-1) + Fn-2
    return ((4 * even_fib(n-1)) + even_fib(n-2)) 


# Driver Code
print(even_fib(14))


print("\n")


print('Function which counts Eulers number:')

def euler(n):
    r = n
    i = 2
    while i*i <= n:
        if n % i == 0:
            while n % i == 0:
                n //= i
            r -= r//i
        else:
            i += 1
    if n > 1:
        r -= r//n
    return r
 
print(euler(112))
print(euler(199))


print("\n")


print('Lesser primes:')

def count_lesser_primes(n):
    ctr = 0
    for num in range(n):
        if num <= 1:
            continue
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            ctr += 1
    return ctr

print(count_lesser_primes(10))
print(count_lesser_primes(100))
print(count_lesser_primes(1000))


print("\n")


print('Sum of prime numbers lesser than 1000:')

def is_prime(number):
    amount_of_factors = 0
    for candidate_factor in range(1, number+1):
        if number % candidate_factor == 0:
            amount_of_factors += 1

    if amount_of_factors == 2:
        return True
    else:
        return False

prime_total = 0
#generates a list of numbers.
for number in range(1000):
    if is_prime(number):
        prime_total += number

print(prime_total)


print()


print('sum of nums divisible by 3:')

def primes_sum(lower, upper):
    total = 0
    for num in range(lower, upper + 1):
        if not num % 3 and num % 10:
            continue
        elif num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                total += num
    return total

total_value = primes_sum(0, 1000)
print(total_value)


print()


print('Primes sum exept 3:')

def primes_sum(lower, upper):
    """Assume upper>=lower>2"""
    primes = [2]
    answer = 2
    for num in range(lower, upper+1):
        if any(num % p == 0 for p in primes):
            continue # not a prime
        elif num < 2:
            continue

        primes.append(num)

        if '3' in str(num):
            continue
        answer += num

    return answer

print(primes_sum(3, 1000))


print('\n')


print('Divisors:')

def divisors(n):
    for i in range(1, n+1):
        if n % i == 0:
            print(i)

divisors(23)
print()
divisors(24)


print('\n')


print('Sum of nums:')

def sum_info(n):
    total = 0
    for i in range(1, n+1):
        if i == n:
            print(i, end="=")
        else:
            print(i, end="+")
        total += i
    print(total)

sum_info(10)
sum_info(12)
sum_info(14)
sum_info(18)


print('\n')


print("Program to find the number less than 1000 with the most factors.")

factlist = [] # Create a list of factors of each number 1 to 999. 
for n in range(1,1000): 
    countfact = 0   # Reset the number of factors.  
    for i in range(1,n+1): 
      if n % i == 0: # If i is a factor of n.. 
        countfact += 1 # Increment the factor count of n. 
        
    factlist += [countfact] # Put the factor count of n in the list of factors. 
print("")     
maxfact = max(factlist)  # Find the maximum factor in the list of factors. 
for k in range(999):     # Find the number which has the maximun factors. 
   if factlist[k] == maxfact: 
      print(k+1, "has", maxfact, "factors which is the most for numbers 1 to 999.")


print('\n')


def is_3square(n):
    while n > 0 and n % 4 == 0:
        n //= 4
    return n % 8 != 7

for i in range(1000):
    if not is_3square(i):
        print(i, end=', ')

print()


print('\n')


print('Powers are:')

def powers(base, n):
    for pw in range(1, n+1):
        print(base**pw)

powers(2, 7)
print()
powers(3, 5)
print()
powers(9, 2)


print('\n')


print('Num 53 divisors sum:')

def compute_53_sum(n):
    res = sum(x for x in range(n) if x % 53 == 0)
    print(res)

compute_53_sum(53)
compute_53_sum(200)
compute_53_sum(300)


print('\n')


print('Listing prime numbers:')

def print_primes(n):
    primes  = []
    chk = 2
    while len(primes) < n:
        ptest = [chk for i in primes if chk%i == 0]
        primes += [] if ptest else [chk]
        chk += 1
    for i in primes:
        print(i)
    print()

print_primes(10)
print()
print_primes(100)


print('\n')


print('The highest sum of two consecutive numbers in list of positive numbers:')


def max_pair_sum(num_list):
    n = len(num_list)
    if num_list[0] > num_list[1]:
        first = num_list[0]
        second = num_list[1]
    else:
        first = num_list[1]
        second = num_list[0]

    for i in range(2, n):
        if num_list[i] > first:
            second = first
            first = num_list[i]
        elif num_list[i] > second and num_list[i] != first:
            second = num_list[i]
 
    return (first + second)

print(max_pair_sum([1, 8, 7, 3, 5, 2]))
print(max_pair_sum([1, 2, 45, 4, 5, 6, 7, 3, 2]))


print('\n')


print('Decomposed product of prime numbers:')

def factoriz(n):
    j = [] #list for prime numbers
    lst = [] #list for factors for numbers in range(n)

    # prime numbers
    for number in range(2, n+1):
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            j.append(number)

    #factors
    for c in range(n, n+1):
        print(f'{c} =', end=' ')
        lst = []
        for i in j:
            while i <= c and c % i == 0:
                c //= i
                lst.append(i)

        print(*lst, sep=' * ')

factoriz(19)
factoriz(75)
factoriz(102)
factoriz(1001)
factoriz(360)

print()

def factorize1(n):
    j = []
    lst = []

    for number in range(2, n+1):
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            j.append(number)

    for c in range(n, n+1):
        print(c, '=', end=' ')
        lst = []
        for i in j:
            while i <= c and c % i == 0:
                c //= i
                lst.append(i)

        print(*lst, sep=' * ')

factorize1(19)
factorize1(75)
factorize1(102)
factorize1(1001)
factorize1(360)

print()

def factorize(n):
    c = 2
    while(n > 1):
        if(n % c == 0):
            print(c, end=' ')
            n = n / c
        else:
            c = c + 1

factorize(19)
factorize(75)
factorize(102)
factorize(1001)
factorize(360)


print('\n')


print('The most common element:')

def most_common(mylist):
    counter = 0
    num = mylist[0]

    for i in mylist:
        curr_frequency = mylist.count(i)
        if(curr_frequency > counter):
            counter = curr_frequency
            num = i

    return num

print(most_common([3, 7, 1]))
print(most_common([3, 7, 5, 3, 1, 2, 3, 1, 7]))
