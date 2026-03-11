'''Read a num from the user and print all the factors for that number.
 input: 12
 output: 1 2 3 4 6 12'''
'''
n = int(input())
for i in range(1, n//2 + 1):
    if n % i == 0:
        print(i, end=' ')
print(n)
'''

'''count the number of factors for a given number
input: 12
output: 6'''
'''
n = int(input())
counter = 0
for i in range(1, n//2 + 1):
    if n % i == 0:
        counter += 1
print(counter + 1)
'''

'''read a num from user and check if the num is prime or not
input: 12
output: Not prime'''
'''
n = int(input())
counter = 0
for i in range(2, n//2+1):
    if n % i == 0:
        counter += 1
#print("prime" if counter == 0 else "not prime")
if counter == 0:
    print("Prime")
else:
    print("Not prime")
'''

'''display all the prime numbers in the given range and also include start and stop
intput: 1 10
output: 2 3 5 7'''
'''
start = int(input())
end = int(input())
if start == 1:
    start = 2
for n in range(start, end + 1):
    counter = 0
    for i in range(2, n//2+1):
        if n % i == 0:
            counter += 1
    if counter == 0:
        print(n, end=" ")
'''

'''Factorial of a number  0 --> 1, 1--> 1, -ve--> no factorial
input: 5
output: 120'''
n = int(input())
if n < 0:
    print("No factorial")
elif n == 0 or n == 1:
    print(1)
else:
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    print(fact)

