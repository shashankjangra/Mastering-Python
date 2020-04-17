lim = int(input('Enter the limit \n'))
lis = []
for i in range(0,lim):
    ele = int(input())
    lis.append(ele)

print(lis)
ctr = 0
for i in range(len(lis)):
    # print('I = ' + str(lis[i]))
    for j in range(len(lis)):
        # print('J = ' + str(lis[j]))
        if lis[i] == lis[j]:
            ctr = ctr+1
            # print(str(ctr))
        
    if ctr==1:
        print(lis[i])
    ctr = 0
