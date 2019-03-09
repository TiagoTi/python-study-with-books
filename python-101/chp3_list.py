# create list
my_list = []
my_list = list()

#combine list - 1
l1 = [1,2,3]
l2 = [1,3,5]
l1.extend(l2)
print(l1)

#combine list - 2
l1 = [1,3,5]
l2 = [2,4,6]
combo = l1 + l2
print(combo)


#sort list
print('sorting list')
l1 = [1,3,5,2,4,6]
print(l1)
l1.sort()
print(l1)


#slice list
print('slice')
l1 = [0,1,2,3,4,5,6,7,8,9]
print('zero-eight',  l1[0:9], 'no show nine')
print('one-nine',  l1[1:10], 'no show zero')
print('three-seven',  l1[3:8])
