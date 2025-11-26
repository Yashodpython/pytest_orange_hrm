# name = 'Ramesh'
# name1 = ""
# for i in name:
#     print(i)
#     if i not in name:
#         if i.isupper():
#             i=i.lower()
#             print(i)


#1.take string as your name in varaible
#2.and find vowles if there in your string
#3.and count each vowel char how many times it hs repated in your string


a='Ramesh'
vowels='aeiou'
#d={'a':1,'e':1}
d={}
for char in a:
    if char in vowels:
        count=a.count(char)
        d[char]=count
print(d)

##############################################################################
# l1 = ['a', 'b', 'b', 'b', 'c', 'c', 'a', 'c', 'c', 'a']
# "a =1, b = 3, c = 2, a =1, c= 2, a = 1"
# str1 = ""
# count = 1
# for i in range(0, len(l1) - 1):
#     if l1[i] == l1[i + 1]:  # 'b' == 'c'
#         count = count + 1  # c=3
#     else:
#         str1 = str1 + l1[i] + " " + "=" + str(count) + " , " # str1 = 'a =1b =3'
#         count = 1
# str1 = str1 + l1[i + 1] + " " + "=" + str(count)
# print(str1)
# l2=str1.split(',')
# #print(l2)
# str2 = " ' ".join(l2)
# print(str2)


# Output = a =1b =3c =2a =1c =2a =1

"""
   *
  * *
 * * * *
* * * * *
"""

# for i in range(0, len(5)):


