def fizzBuzz(n):
    # Write your code here
    n=n+1
    for i in range(1,n):
        if (i%3==0) and (i%5==0):
            print('FizzBuzz')

        if (i%3==0) and (i%5!=0):
            print('Fizz')

        if (i%5==0) and (i%3!=0):
            print('Buzz')

        if (i%3!=0) and (i%5!=0):
            print(i)
