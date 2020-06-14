while True:
    try:
        T = int(input())
        if T<1 or T>10:
            raise ValueError
            
        break
    except ValueError:
        continue
    
S = []
while True:
        try:
            len_S = len(S)
            if len_S >= T:
                break
            
            temp_S = input() 
            
            if len(temp_S)>=2 and len(temp_S)<=10000:
                S.append(temp_S)
            
            if len(temp_S)<2 or len(temp_S)>10000:
                raise ValueError
        
        except ValueError:
            continue
        
even_S = ''
odd_S = ''
for i in range(T):
    temp_S = S[i]
    for j in range(len(temp_S)):
        if j%2 == 0:
            even_S = even_S + temp_S[j]
            
        else:
            odd_S = odd_S + temp_S[j] 
            
    print("{} {}".format(even_S,odd_S))
    even_S = ''
    odd_S = ''
            
    