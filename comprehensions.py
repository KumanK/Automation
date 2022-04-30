list_of_list = [[1,2,3],[4,99,6],[7,8]]
L=[ele for chunk in list_of_list for ele in chunk]
print L

L = [x for x in range(100) if x%5==0 if x%10==0]
print L

L = [x if x%2 ==0 else -1 for x in range(10)]
print L

L = [6,3,4,5]
l1= map(lambda x:x**x,L)
print l1
l1 = [x**x for x in L]
print l1

L = [3,6,59,2,4,9,0]
l1=filter(lambda x:x%3,L)
print l1
l1=[x for x in L if x%3 !=0]
print l1