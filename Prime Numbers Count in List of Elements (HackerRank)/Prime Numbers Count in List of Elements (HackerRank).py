def countPrimeNumbers(numbers):
    ctr = 0
    prime = 0
    for i in numbers:
        for j in range(1,(i+1)):
            
            k = int(i%j)
            if (k == 0):
                ctr = ctr+1
            
        if (ctr == 2):
            prime = prime+1
        
        ctr = 0
    return prime
                
    

if __name__ == '__main__':
    numbers=[]
    count=int(input())
    for i in range(count):
        numbers.append(int(input()))
        
    print(countPrimeNumbers(numbers))
        
