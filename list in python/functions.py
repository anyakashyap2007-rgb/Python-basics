day_of_week =["mon","tue","wed","thus","fri","sat","sun"]
print(day_of_week)

#reverse()
day_of_week.reverse()
print(day_of_week)

#sort()
num =[7,8,0,1,2,3]
print(num)
num.sort()
print("sorted list:",num)
num.sort(reverse=True)
print(num)

#count()
numbers = [0,1,3,4,1,0,5,0,3,3,0]
print(numbers.count(0))

#user input 
print(f"the list is:{numbers}")
item_to_count= int(input("enter the numer to be counted from the list:"))
c= numbers.count(item_to_count)
print(f"occurrence of {item_to_count} is {c}")

#Membership operation

#in fuction ,not in 
language =["C++","Python","English"]
print("C++" in language)
print("hindi" not in language)