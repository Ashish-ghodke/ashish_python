# 2. PROGRAM TO CHANGE VOWELS PRESENT IN THE STRING BY @ SIMBOL 

str = "hello world my name is ashish "
vowel = "aeiouAEIOU"
str2 = " "
n = len(str)
for i in range(n):
    if str[i] in vowel:
       str2 += "@"
    else:
        str2 += str[i]
        
print(str2)


# using while loop 

i = 0 
while i< n:
    if str[i] in vowel:
        str2 += "@"
        i+= 1
    else:
        str2 += str[i]
        i += 1
print(str2)