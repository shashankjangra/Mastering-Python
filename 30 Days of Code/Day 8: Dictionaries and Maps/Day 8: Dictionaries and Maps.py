while True:
    try:
        n = int(input())
        if n<1 or n>100000:
            raise ValueError
        break
    except ValueError:
        continue
phone_book = {}
while True:
    try:
        phone_book_len = len(phone_book)
        if phone_book_len >= n:
            break
        
        phone_book_raw = input()
        x,y = map(str, phone_book_raw.split())
        
        if len(x)>1 and len(x)<100000:
            phone_book[x] = y
            
        else:
            raise ValueError
            
    except ValueError:
        continue
        
       
while True:
    try:
        query = input()
        if query in phone_book:
            print("{}={}".format(query,phone_book[(query)]))
        
        else:
            print('Not found')

    except:
        break
