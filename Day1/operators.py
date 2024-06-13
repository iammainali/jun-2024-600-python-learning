# hash symbol is used to comment out the description of the python code.
# Python code can be executed from two different ways:-
# 1. python shell
# 2. using file with python extension(.py)

a = 1
b = 2
print(a+b)  # print() is a built in function
print("hello world")


# operators in python
# 1. Arithmetic (+,-,/,*,//,%,**)
# 2. relational
# 3. logical
# 4. assignment
# 5. membership
# 6. identify


# the result of relational operator is always boolean ie true or false
a = 10
b = 4
c = a > b
print(c)  # true

print(a != b)  # true
print(a == b)  # false

print(a >= b)  # true
print(a <= b)  # true

# logical operation

# and , or , not
# and operation
# e1   e2   result
# t     t     t
# t     f     f
# f     t     f
# f     f     f

# membership operator is used to check whether an element is a member of a sequence or not
# result of membership operation is also true or false
# 'in' or 'not in' are the membership operators

a = [1, "a", "hello", 2.5, -4]
b = 2

print(b in a)  # false
print("A" in a)
print("hello" in a)
print("b" not in a)
print("hello" not in a)


# identity operator
# it checks whether two or more data have same reference (memory location) or not
