"""
-->List is collection data type (it sotres more than value)
-->List is mutable data type
-->List follows index order(either positive or negative)
-->List allows duplicates
"""

"""
List methods : append ,remove, ,index ,insert ,reverse,sort ,count ,extend
"""
l1=[1,2,3,4,['list1','list2']]
# len: it counts the length of elements availble in given object ,it counts from 1
print(len(l1))
l1[0]=100
print(l1)


l2=[10,20,30,40,70.8]

#append() :it will add given data to the list ,by default it added at end of the list.

l2.append("ganga")
print(l2)

l2.append([1000,2000])
print(l2)

#remove(): It will remove the first occurance of element which value you specified in remove method
#syntax : object.remove(value)
l3=[1,2,3,4,3]
l3.remove(3)
l3.remove(4)
print(l3)
#l3.remove("apple") -->Value Error if given value is not exist

#count : it counts the given element how many times it is repeated

l1=['a','b','c','d','a','e','f']

count_element=l1.count('a')
print(count_element)
count_element2=l1.count(2)
print("count_element",count_element2)


#index() :it find the first match element index position in a given list
l1=['a','b','c','d','a','e','f']
ind_pos=l1.index('a')
print(ind_pos)


#extend() :it will merger  list into another list

l1=[1,2,3,4,5]
l2=[6,7,8]

#l1.extend(l2)
#l2.extend(l1)
l3=l2+l1
print(l3)

#reverse() :it will reverse the elements of given list
l1=[5,6,7,8,9]
l1.reverse()
print(l1)

#pop : pop method will remove value/element based on index position , by default it take last element index position.
l1=["Bob","john","king"]
pop_value=l1.pop()
print(pop_value)
print(l1)
pop_value=l1.pop(0)
print(pop_value)
print(l1)

#what is d/f b/w remove and pop
l1=[10,20,30,20,40,10]
l1.remove(20)
print(l1)


#sort() :it will sort the numbers in ascending order by default .

l1=[10,1,9,2,5]
# l1.sort()
# print(l1)
l1.sort(reverse=True)
print(l1)

#type of arguemnts

#default argument
def add(a,b=10,c=20):
    return a+b+c
print(add(10))
print(add(10,20,30))

# slicing Topic
#it will slice the given object(list) into the parts
#slice syntax :obj[start,end,step]
l1=[10,30,40,60,10]
part1=l1[0:4]
part2=l1[len(part1)::]
print(part1)
print(part2)
l2=['a','b','c','d','e']
print(l2[-1::-1])
print(l2[-2:-5:-1])


#using positive slicing will take step is 2

numbers =[1,2,3,4,5,6,7,8,9,'202']
print(numbers[::3])
print(numbers[::-3])

l1=[1,2,3,4]
#find the length of list (l1)
print(len(l1))
len_l1=len(l1)
cut_last_two_elemnts=len_l1-3
print(l1[:cut_last_two_elemnts])
# l1.pop()
# l1.pop()
#print(l1)
#tuple :















