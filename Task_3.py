n = int(input('Введите номер билета: '))
a6 = n%10
a5 = n//10%10
a4 = n//100%10
a3 = n//1000%10
a2 = n//10000%10
a1 = n//100000
if a1 + a2 + a3 == a4 + a5 +a6:
    print('yes')
else:
    print('no')
