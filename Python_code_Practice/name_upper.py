# def make_upper(func):
#     def wrapper():
#         res = func()
#         return res.upper()
#     return wrapper
#
#
# @make_upper
# def my_name():
#     return "ramesh"
# print(my_name())
# def my_doc(func):
#     def wrapper():
#         res = func()
#         return res.capitalize()
#     return wrapper
#
# @my_doc
# def my_name():
#     return "ramesh"
# print(my_name())