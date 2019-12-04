lst = [] 
n = int(input("Enter total number of elements : ")) 
  
for i in range(0, n): 
    ele = int(input())
    lst.append(ele) 
      
print("given list:",lst) 
lst.sort()
print("sorted list:",lst)


if(n%2!=0):
    print("median is:",lst[int(n/2)])   #use // floor option
else:
    med=lst[int(n/2)]+lst[int(n/2)-1]
    print("median is:",med/2)
