num = [2, 4, 6, 10]
def square(num):
    return num*num
x = map(square, num)
y = list(x)
print(y)