def swap (a,b):
    a = a^b
    b = a^b  # (a^b)^b == a 
    a = a ^ b 
    return a,b



x = 5

y = 10

print(swap(x,y))

