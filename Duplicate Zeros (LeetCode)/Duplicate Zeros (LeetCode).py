
arr = [1,0,2,3,0,4,5,0]

i = 0
while True:
    if i>=len(arr):
        break
    
    if arr[i] == 0:
        arr.insert(i+1, 0)
        i = i+2
        arr.pop()
    
    else:
        i = i+1