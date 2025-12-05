"""
Functions is a reusable block of code
It does a specific task
It will only execute when it calls.
After return statement ,if any code lines will be there it wont execute because of when return is executed
it terminate function
if return not retrieve anything the output is None

"""
print(len("string"))  #6
print(len(["1","2","3","4"]))#4
print(len({"1":2,2:3,(1,2,3):(1,2,3)}))#3
print(len(("tp1","tp2")))#2
print(len({"1",2,3,4,5,6,88,6}))#7

#without using inbuilt len() function please count the element of give data object

def fiding_length_of_data_object(data_obj):
    c=0
    for ele in data_obj:
        c=c+1
    return c
print(fiding_length_of_data_object("hello"))
print(fiding_length_of_data_object([1,2,3,4,5,6,7,8]))
print(fiding_length_of_data_object({"1":2,2:3,(1,2,3):(1,2,3)}))
"""
def functionaname(para1,para2,paraan):
   statements 
   stamentnts
   return [to return the value]
#calling funnction
functionaname(arg1,arg2,argn)
"""
# #add two integer values using function.
# def add(int1,int2):
#     sum = int1+int2
#
#     return sum
#     print(sum)  # 30
#
# print(add(10,20))
#
#
# def func1():
#     print("return1")
#     return 1
#     print("reutnr 2")
#     return 2
# print(func1())
#
#
# def func2():
#     c=10+20
#     if c % 2 ==0:
#         return True
#     else:
#         print("False")
# print(func2())
#
# def func3(a,b):
#     if False:
#         return False
#     elif False:
#         if 5 <4:
#             print("return False")
#     elif False:
#         pass
#     else:
#         if a>b:
#             print(True)
#             return a
# print(func3(4,3))
#
#
#

l1=[1,2,3,4]
print(l1.index(3))


list1 = [1, 23, 5, 10, 2, 4]
def finding_index_value(list_obj, ele):
    c = -1
    for i in list_obj:
        c += 1
        if i == ele:
            return c
print(finding_index_value(list1, 5))