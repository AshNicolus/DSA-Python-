def convert2decimal(x)-> str:
    n = len(x)
    num = 0
    p2 = 1
    for i in range(n-1,-1,-1):
        if (x[i]=='1'):
            num = num + p2 
        p2 = p2 * 2
    return num

str = '1010'

print(convert2decimal(str))