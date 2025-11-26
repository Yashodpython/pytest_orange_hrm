#split() :
"""
The split() method splits a string into a list.
By default, it separates the string wherever there is a space.
You can also specify a different separator to split the string with a chosen character

"""

str1="Hi Hellow world"

#I am going to split without any delimeter or separator , by default it will split by wherever have spaces

c_list=str1.split()
print(c_list) #['Hi','Hellow','world']

str2='sudharsan'

split_with_a_char=str2.split('a')
print(split_with_a_char) #['sudh','rs' ,'n']

str3='anbcandean'
split_with_a_char=str3.split('an')
print(split_with_a_char) #['', 'bc', 'de', '']

#Exercise:
str4="Hello Bangalore , welcome to winter season"

#0/p ["Bangalore" ,"welcome" ,winter" ,"season"]

c_words=str4.split() #['Hello','Bangalore' , ',', 'welcome', 'to', 'winter' , 'season']
print(c_words)
l1=[]
for word in c_words:
    if word !='Hello' and word !=',' and word !='to':
        l1.append(word)
print(l1)

str5="Hi Hello How are you"
#o/p ['i','ello','ow' ,'are','you']

#startswith :It checks whether the string begins with the given argument.

str1="Hi Hello"
print(str1.startswith('Hello'))
print(str1.startswith('H'))

#endswith :It checks whether the string ends with the given argument.

str2="welcome to banglore"
print(str2.endswith('ore'))
print(str2.endswith('o'))

#strip() : it will remove spaces at beginning and ending of the string only
#rstrip :it will remove spaces at right-side of the string only
#lstrip :it will remove spaces at left-side of the string only

name ="  obulesh    "
print(len(name))
strip_action=name.strip()
print(strip_action,len(strip_action))

#join() ,isalnum,isalpha

list_of_list=[2, 3,[8,9,[4, 5,[6,7]]]]
flat_list=[]
for item in range(len(list_of_list)):
    if type(list_of_list[item])!=list:
        flat_list.append(list_of_list[item])
    elif type(list_of_list[item])==list:
        for i in range(len(list_of_list[item])): #[8,9,[4, 5,[6,7]]]
            # 0,1,2
            #[8,9,[4, 5,[6,7]]]
            if type(list_of_list[item][i])!=list:
                flat_list.append(list_of_list[item][i])
            elif type(list_of_list[item][i])==list:

                for j in range(len(list_of_list[item][i])):
                    # [4, 5,[6,7]]
                    if type(list_of_list[item][i][j]) != list:
                        flat_list.append(list_of_list[item][i][j])
                    elif type(list_of_list[item][i][j]) == list:
                        for k in range(len(list_of_list[item][i][j])):
                            #[6,7]
                            if type(list_of_list[item][i][j][k]) != list:
                                flat_list.append(list_of_list[item][i][j][k])


print(flat_list)

