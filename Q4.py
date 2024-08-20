# # 4. SORT THE STRING IN ALPHABETICAL ORDER WITHOUT USING SORT FUNCTION 



s = "hello my name is ashish"
a = s.split()
for i in range(len(a)):
    for j in range (i+1, len(a)):
        if a[i]>a[j]:
            a[i],a[j] = a[j],a[i]
print(a)    
    
    
    
