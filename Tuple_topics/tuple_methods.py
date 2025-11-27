"""
                Tuple Topics

Tuple Data type Definition:

--->It is a collection data type in Python.

-->It is ordered (the order of elements is fixed).

-->It is indexed (you can access elements using index).

-->You can retrieve elements using positive indexing and negative indexing.

-->It allows duplicate values.

--> it is immutable (you cannot change, add, or remove elements after creation).

-->It can store multiple data types (int, string, float, etc.).

-->It takes less memory and is faster than a list.

-->It is written using round brackets ( ).or paranthesis()

"""

#Note :To create single element in tuple

t = (10,)
print(type(t))   # <class 'int'>

#Note to create empty tuple
t2= ()
print(type(t2))

#Conversion form tuple to list

t3 =(10,20,30,40)
c_list=list(t3)
print(c_list)
c_list.append(50)
t4=tuple(c_list)
print(t4)

#Note :In tuple data have only two methods
#1.index 2.count

#index() : it will retrieve first occur of element index position in given object.

t5=(10,20,10,30,20,10)
print(t5.index(10))
print(t5.count(10))
#t5[0]=100 #TypeError: 'tuple' object does not support item assignment

