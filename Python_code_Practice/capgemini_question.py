Roles = {
    "cust1": ["RESS|787815|Acc|2024-07-12", "UNRS|787812|Acc|2024-07-12"],
    "cust2": ["PRI|665590|Acc|2024-07-12", "UNRS|787815|Acc|2024-07-12"],
    "cust3": ["RESS|324567|Acc|2024-07-12", "UNRS|234562|Acc|2024-07-12"],
}

#res = {787815:['RESS','UNRS'],787812 :[UNRS] ,665590 :[PRI],324567: ['RESS'] ,234562 :['UNRS']}
# d={1:2}
# d[1]
# res={}
# for role in Roles:
#     for item in Roles[role]:
#         split_value = item.split("|")
#         if split_value[1] not in res:
#             res[split_value[1]] = [split_value[0]]
#         else:
#
#             res[split_value[1]].append(split_value[0])
# print(res)

d={1:[2],2:[3]}
d1={1:3,4:5,7:8}
d2={}
#0/p ={1:[2,3],2:[3],4:5,7:8}
for i in d1:
    # print(d1[i])
    if i in d:
        d[i].append(d1[i])
        print(d)
        d2[i]=d[i]
    else:
        d2[i]=d1[i]
for i in d:
    if i not in d2:
        d2[i]=d[i]
print(d2)

d={1:2,3:4,5:6,7:8}



