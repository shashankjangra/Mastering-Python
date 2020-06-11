#Input N
while True:
    try:
        N = int(input())
        if N<=1 or N>=500:        
            raise ValueError
        break
        
    except ValueError:
        print("Wrong")

#Input the Array of Numbers
nums = []
for i in range(0,N*2):
    nums.append(int(input()))
    
final = []    
for i in range(0,N):
    final.append(nums[i])
    final.append(nums[i+N])
    
print(final)