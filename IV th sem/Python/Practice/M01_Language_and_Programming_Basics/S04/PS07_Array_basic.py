'''import array
arr = array.array('i',[])
print(arr, type(arr))
arr.append(10)
arr.append(20)
print(arr)
arr.append(12.45) #gives error
'''
'''
List:
1. use  [] to create list.
2. list is mutable.
3. list allows duplicate values.
4. list is heterogenous.
5. list is indexed.
'''
'''
li = [12,25.4,6+5,"Hello",12,25.4]
print(li,type(li)) # --> <class 'list'>
print(li[3]) #--> Hello
print(li[3:6]) # --> [Hello, 12, 25.4]
print(li[::-1]) # --> reverse order
print(len(li)) # --->length of the list 6
li.append(100) 
print(li) # --> [12, 25.4, 11, 'Hello', 12, 25.4, 100]
#li.insert(2, "world")
#print(li)
#li.insert(10, "world")
#print(li)
li.insert(-20, "world")
print(li)
'''
#Read a num from the user and display num of digits in that num
#input : 1234
#output : 4
x = int(input())
print(x, (x))
