lst = [4,5,3,1,3,4,7,4,8,5,3,0]
n = len(lst)
for i in range(n):
    for j in range(i+1,n):
        if lst[i] > lst[j]:
            lst[i],lst[j] = lst[j],lst[i]

print(lst)