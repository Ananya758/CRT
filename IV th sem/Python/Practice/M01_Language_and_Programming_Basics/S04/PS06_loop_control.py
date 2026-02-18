'''for i in range(1, 11):
    #print(i, end=" "); #---> 1 2 3 4 5
    if i == 5:
        break
    print(i, end=" "); #----> 1 2 3 4'''

'''for i in range(1, 11):
    if i == 5:
        continue
    print(i, end=" "); #----> 1 2 3 4 5 6 7 8 9 10'''

'''for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end=" "); #--->1 3 5 7 9'''

'''Password retry system(max 3 attempts) 
   if password is correct show login successful
   else ask for password 3 times.
   Once attempts exceed show account locked!'''

x = "Pass123"
for i in range(3):
    t = input()
    if t == x:
        print("login successful")
        break
else:
    print("Account locked")
    
