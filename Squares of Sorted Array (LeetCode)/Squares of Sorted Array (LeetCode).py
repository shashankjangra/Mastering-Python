N = int(input("Enter the size of the array: "))
A = []

for i in range(N):
    num = int(input("Enter {} number: ".format(i+1)))
    A.append(num)
    
A_sq = []
for i in range(N):
    num = A[i] * A[i]
    A_sq.append(num)
    

A_sq.sort()
print(A_sq)