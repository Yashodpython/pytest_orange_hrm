"""
                     #dict_defintion
--It is pair of key and value enclose within curly brackets '{'a':'b','a':'c'}
--The key should be unique
--The value can be duplicate
--The key data type should be immutable data type( string,numbers,tuple)
--using key , we can retrieve value
--it is mutable like list
"""
# d={1:2,1:3}
# print(d)
#d={[1,2]:90} #TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
d={'name':'vijay'}
print(d['name'])
d['name']='obulesh'
print(d)

#keys() : it will retrieve all keys of that dictionary object
d={1:2,'name':'obulesh',3:4,'age':40}
print("keys",list(d.keys()))

#values() : it will retrieve all values of that dictionary object
print("values",list(d.values()))

dict1={}
dict1['pincode']=512341
dict1['city']='Bangalore'
print(dict1)

#items() : it will retrieve keys and values as pair withing tuple
print(list(d.items())) #[(1,2) ,('name','obulesh'), (3,4) ,('age'40)]
l3=[(1,2) ,('name','obulesh'), (3,4) ,('age',40)]
#l4=[1,2,'name','obulesh',3,4,'age',40]
l4=[]
l4.extend(l3[0])
l4.extend(l3[1])
l4.extend(l3[2])
print(l4)
# for item in l3:
#     #print(item)
#     for item1 in item:
#         print(item1)
#         l4.append(item1)
# print(l4)
#setdefault(): it used to add new key ,value pair
dict2={}
dict2.setdefault('course','python')
dict2.setdefault('age',40)
print(dict2)

#update: it will update existed dictonary whith given key ,value
dict2.update({'city':'Bangalore'})
print(dict2)
dict2.update({'course':'java'})
print(dict2)