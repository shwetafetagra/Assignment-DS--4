num = [1,2,3,4,5,6,7]
def triple(num):
    return num * 3
num_map = map(triple, num)
list_num = list(num_map)
print(list_num)