def calc (x,y,s) : # Function of the operations
    result = 0 # Store result Var
    if s == "+" : # check if the user choosed +
        result = x+y # get the sum of the numbers and store it in result var
    elif s == "/" : # check if the user choosed /
        result = x/y # get the result of the numbers and store it in result var
    elif s == "*" : # check if the user choosed *
        result = x*y # get the result of the numbers and store it in result var
    elif s == "-" : # check if the user choosed -
        result = x-y # get the result of the numbers and store it in result var
    if result % 2 == 0 and result != 0: # Check if the number was Even 
        print (result,"is even") # Say the number is even
    elif result == 0 : # check if it's zero
        print("It's zero !!!!!!!!!!!!!!!!!!!!") # print it's zero !!!!!!!!!!!!!!!!!!!!!!!!!!!!
    else : # check if it something else (odd number)
        print (result,"is odd") # print it is odd
    return result # get the Result Value
def q(s): # function of the result
    x = int (input ("Enter the frist Number : ")) # get the first number
    y = int (input ("Enter the second Number : ")) # get the second one
    print ("the Value = ",calc (x,y,s)) # print the value 
    return s # return the s var

while True: # loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooop
    s = input("Enter the opretion Symbol (/,*,+,-) or Enter 0 to exit: ") # check the operation symbol that the user wants I hat the user
    if s == "0" : # check if it zero
        break # close the app yayyyy
    else : # else
        q(s) # nana ur buessines 
# lol lmao lmfao :ok-cry: :joy: :crydeath:
