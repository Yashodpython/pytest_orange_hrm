list1 = [1, 23, 5, 10, 2, 4]
def finding_index_value(list_obj, ele):
    c = -1
    for i in list_obj:
        c += 1
        if i == ele:
            return c
print(finding_index_value(list1, 5))