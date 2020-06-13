while True:
    try:
        n = int(input())
        if n<=2 or n>=20:
            raise ValueError
        break
    except ValueError:
        continue
    
for i in range(1,11):
    print("{} x {} = {}".format(n,i,n*i))