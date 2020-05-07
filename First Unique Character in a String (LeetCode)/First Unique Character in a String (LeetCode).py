s = input("Enter the String: ")
ctr = 0
x = len(s)
print(x)
arr =[]

if s == '':
    print('-1')
    # return -1
    
for i in range(x):
    print(i)
    for j in range(x):
        # print(j)
        if s[i] == s[j]:
            ctr = ctr+1
    arr.append(ctr)
    if 1 in arr:
        if arr[i] == 1:
            print(i)
            # return i
            break
    ctr = 0
        
for i in range(len(arr)):
        
    if 1 not in arr:
        print('-1')
        # return -1
        break


