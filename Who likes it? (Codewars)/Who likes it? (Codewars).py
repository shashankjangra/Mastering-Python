def likes(names):
    #your code here
    names_len = len(names)
    
    if names_len == 0:
        return "no one likes this"
    
    if names_len == 1:
        return "{} likes this".format(names[0])
        
    if names_len == 2:
        return "{} and {} like this".format(names[0],names[1])
        
    if names_len == 3:
        return "{}, {} and {} like this".format(names[0],names[1],names[2])
        
    if names_len > 3:
        val = names_len - 2
        return "{}, {} and {} others like this".format(names[0],names[1],val)