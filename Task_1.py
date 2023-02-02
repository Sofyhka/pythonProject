k =int(input('Введите трёхзначное число: '))
c = k % 10
k = k // 10
b = k % 10
a = k // 10
print(a + b + c)