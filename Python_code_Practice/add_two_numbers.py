# def addition_one_extra_value(func):
#     def wrapper(a, b):
#         c = 10
#         res = func(a, b) + c
#         return res
#     return wrapper
#
# @addition_one_extra_value
# def add_two_numbers(a, b):
#     return a + b
# print(add_two_numbers(1, 2))


def add_name(func):
    def wrapper(a,b):
        c = 20
        res = func(a, b) + c
        return res

@add_name
def my_name(a, b):
    return a + b
print(my_name(10, 20))


