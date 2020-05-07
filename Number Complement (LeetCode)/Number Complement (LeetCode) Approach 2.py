num = 10
a = []
s = ''
t = ''

if num == 0:
    print('1')
    
elif num == 1:
    print('0')

elif num > 1:
    
    while num>1:
        b = int(num%2)
        num = num/2
        a.append(b)
            
    for i in reversed(range(len(a))):
        s = s + str(a[i]) 
        
    for i in s:
        if i == '1':
            t = t +'0'
    
        if i == '0':
            t = t + '1'
        
    t = int(t,2)
    print(t)
