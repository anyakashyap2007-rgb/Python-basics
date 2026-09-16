#nested list - list inside a list
l1 = [ 5,1.5,"python",True,None,[1,2,3],10]
print(len(l1))
print(len(l1[-2]))

#fetching element from list inside list 
print(l1[-2])
print(l1[-2][0])

l2=[[1,2],[3,4],[5,6,[0,1]]]
print(len(l2))
print(l2[-1])
print(l2[-1][2]) 
print(l2[-1][2][1])