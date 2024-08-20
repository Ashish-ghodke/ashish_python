# 9. WRITE A PROGRAM TO ACCEPT A STIRNG FORM THER USER AND DISPLAY CHARACTERS THAT ARE PRESENT AT AN EVEN INDEX NUMBER 
#    FOR EXAMPLE , STR = "pynative" SO YOU SHOULD DICPLAY 'p','n','t','v'

s = str(input("Enter a string here : "))
print(f"original string is : {s}")
a = len(s)
# for i in range(0,a,2):
#     print(f"at index {i} we have {s[i]}")

count = 0    
while count < a:
    if count%2 == 0:
        print(f"at index {count} we have {s[count]}")
    count += 1 