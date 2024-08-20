# 10. WRITE A PROGRAM TO REMOVE CHARACTERS FROM A STRING STARTING FROM ZERO UP TO N  AND RETURN A NEW STRING J
    # FOR EXAMPLE IN INPUT IS REMOVE CHARS( "PYNATIVE ", 4) SO OUTPUT MUST BE "TIVE"
    
s = "pynative"
print(f"original string is : {s}")
b = len(s)
num = int(input("Enter a number of character you want to remove form string : "))
if num > b:
    print(f"number should be less than lenth of string lenght of stirng is : {b}")
else:
    x = s[num:]
    print(x)