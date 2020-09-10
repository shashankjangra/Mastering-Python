n = int(input("Enter the number: "))


def check(n):
    fibonnaci = int
    old = 1
    oldest = 0
    if n == 0 or n == 1:
        print("yes")
        return True
    
    else:    
        while True:
            
            fibonnaci = oldest + old
            oldest = old
            old = fibonnaci
            
            if n == fibonnaci:
                print("yes")
                return True
                
            elif fibonnaci > n:
                print("no")
                return False
                   
            
check(n)