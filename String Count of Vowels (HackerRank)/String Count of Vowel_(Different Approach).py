a = input()
b = a.lower()
ctr = 0

for i in b:
    if (i == "a") or (i == "e") or (i == "i") or (i == "o") or (i == "u"):
        ctr=ctr+1
    
print(ctr)