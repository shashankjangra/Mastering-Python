J = input("Input J")
S = input("Input S")

j = len(J)
s = len(S)
ctr = 0

for i in J:
    for k in S:
        if (i==k):
            ctr = ctr+1
print(ctr)