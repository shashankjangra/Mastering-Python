N= int(input("Enter the Array size:"))

nums = []
for i in range(N):
    nums.append(int(input()))

output =0
max_output = 0
for i in nums:
    if i==1:
        output = output+1
        
    if i==0:
        output =0
        
    
    if max_output < output:
        max_output = output
        
print( max_output)