# copy method in python list

a = [1,2,3,4]
b = a  # this is passed by reference
print(a is b) #True

b.append(5)
print(a) #[1,2,3,4,5]

b = a.copy() # pass by value
b.append(6)
print(b) #[1,2,3,4,5,6]
print(a) #[1,2,3,4,5]


# But there are two types of copy
# Shallow copy
# Deep copy

#from copy import deep copy

sum()


b = deepcopy(a)




