from re import I


list1 = [1,2,3,4,5,6,7,8]
 
evanlist =[]

oddlist = []
 

for num in list1:
     

    if (num % 2 == 0):
        evanlist.append(num)
    else:
        oddlist.append(num)
 
    
         
print("Even numbers in the list: ", evanlist)
print("Odd numbers in the list: ", oddlist)