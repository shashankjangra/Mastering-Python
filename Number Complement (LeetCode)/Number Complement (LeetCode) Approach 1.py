num = 0
a = bin(num)
a = a[2:]
b = ''

for i in a:
    if i == '1':
        b = b +'0'

    if i == '0':
        b = b + '1'

b = int(b,2)
print(b)