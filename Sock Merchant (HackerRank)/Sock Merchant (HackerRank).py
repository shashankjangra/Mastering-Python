N = int(input("Enter the number of elements: "))
A = list(map(int, input().split()))
A = A[:N]

ctr = 0
socks_pair = 0
i = 0
j = 0
while i <= len(A)-1:
    check = A[i]
    while j <= len(A)-1:
        if check == A[j]:
            del A[j]
            ctr+=1
            
            if ctr==2:
                socks_pair+=1
                ctr = 0
            
        else:
            j+=1
    
    
    j = 0
    ctr = 0
    