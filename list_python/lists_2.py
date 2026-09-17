#slicing of list 

l1 =[3,8,1,0,4,9,7,3,6]
print(l1[1:6:1])
print(l1[2:7:2])

#concatenation of lists 
l1 =[1,7,2]
l2 =[0,5]
print(l1 + l2)
print(l2 +l1)

#repetition of lists 
print(l2*3)


#functions in lists 

fruits =["Mango","apple","orange"]
print(fruits)
#append()
#syntax: lists.append(item)

"""fruits.append("banana")
print(fruits)"""

#insert()
#syntax:lists.insert(index,item)

"""fruits.insert(2,"guava")
print(fruits)"""

#extend()-use to add multiple items 
fruits.extend(["Banana","Grapes"])
print(fruits)
#fruits.append(["Banana","grapes"]) -adds items as list inside list
#and count lists all item as one 


#remove()
fruits.remove("orange")
print(fruits)
"""fruits.remove("orange")
print(fruits)"""#-shows error for item removal that is not present in the list 

#pop()
fruits.pop(2)
print(fruits)