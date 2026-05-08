def calc (x,y,s) : 
    result = 0 
    if s == "+" :
        result = x+y
    elif s == "/" :
        result = x/y
    elif s == "*" :
        result = x*y
    elif s == "-" :
        result = x-y
    if result % 2 == 0 and result != 0:
        print (result,"is even")
    elif result == 0 :
        print("It's zero !!!!!!!!!!!!!!!!!!!!")
    else :
        print (result,"is odd")
    return result
def q(s):
    x = int (input ("Enter the frist Number : "))
    y = int (input ("Enter the second Number : "))
    print ("the Value = ",calc (x,y,s)) 
    return s

while True:
    s = input("Enter the opretion Symbol (/,*,+,-) or Enter 0 to exit: ")
    if s == "0" :
        break
    else :
        q(s)
