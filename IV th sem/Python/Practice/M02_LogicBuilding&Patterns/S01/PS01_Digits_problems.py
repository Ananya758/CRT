'''
sample input: 1234
sample output: 4

sample input: 455786
sample output: 6

sample input: 45
sample output: 2
'''
#n = int(input())
#count = 0
#while n > 0:
#    count += 1
#    n = n // 10
#print(count)

#sum of digits
'''
n = int(input())
temp = n
s = 0 
while n > 0:
    s += n % 10
    n //= 10
print(s)
print(sum(map(int, str(temp))))
'''

'''
even and odd digits count
input: 12345
output: 2 3

input: 5588
output: 2 2'''
'''
n = int(input())
even = 0
odd = 0
while n > 0:
    if(n % 2 == 0):
        even += 1
    else:
        odd += 1
    n //= 10
print(even, odd)
'''
'''
input: 546 -> 5+4+6=15 -> 1+5=6
output: 6
input: 783 -> 7+8+3=18 -> 1+8=9
output: 9
n = int(input())
while n > 9:
    n = sum(map(int,str(n)))
print(n)
'''
'''
reversing of number
'''
