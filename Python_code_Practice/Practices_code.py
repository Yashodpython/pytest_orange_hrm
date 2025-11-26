
# nam = "ramesh"
# # output = {'a'=1,'e'=1}
# vowels = 'aeiou'
# output = []
# for char in nam:
#
# def add_extra_future(func):
#     def wrapper(a, b):
#         c = 5
#         re = func(a, b) + c
#         return re
#     return wrapper
# @add_extra_future
# def Add_newnumber(a,b):
#     return a + b
# print(Add_newnumber(20, 30))

l1=[1,2,3,4,5,6,7,8]
l2=["even" if i%2==0 else "odd" for i in l1]
print(l2)

matrix=[[1,2,3],[4,5,6],[7,8,9]]
#[expression for outer_item in outer_list for inner_item in inner_list]
make_into_single_list=[row for num in matrix for row in num]
print(make_into_single_list)


"""
[expression for outer_item in outer_list for inner_item in inner_list]
[expression for outer in outer_list for inner in inner_list if condition]
[expression for i in list1 if cond1 for j in list2 if cond2]


"""
outer = [1, 2, 3]
inner = [10, 20]

for item in outer:
    for num in inner:
        print(item*num, end=" ")

#
# result = [o * i for o in outer for i in inner]
# print(result)

#[10, 20, 20, 40, 30, 60]
#[10, 20, 20, 40, 30, 60]
#[10, 20, 20, 40, 30, 60]