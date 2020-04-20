number = (input('Enter the Number: \n'))
n=0
b=0

while n!=1:
    for i in number:
        a = int(int(i)**2)
        b = a+b
    
    number = str(b)
    n=b
    a=0
    b=0