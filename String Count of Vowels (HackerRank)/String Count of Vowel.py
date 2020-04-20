inp_str = input()
ctr = 0
vowels = 'aeiouAEIOU'
for i in inp_str:
    if i in vowels:
        ctr = ctr+1
    
print(ctr)