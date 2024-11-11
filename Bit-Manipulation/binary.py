def convert2Binary( x )->str:
    res = ""
    while(x>0):
        res = str(x%2)+res
        x //= 2

    if res == "":
        return "0"
    else:
        return res
    

string = 100
print(convert2Binary(string))
