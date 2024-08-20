1. # PROGRAM TO ACCESSING INDEX OF LIST USING FOR LOOP


# method 1

lst = [1,2,3,5,6,3,4,6,6]

n = len(lst)
for i in range(0,n):
    print(f"on index {i} we have number {lst[i]}")

# method2
    
for index in range(len(lst)):
    value = lst[index]
    print("at index",index," we have ", value)

# method 3 by using emurate function

for index, value in enumerate(lst):
    print(f"on index {index} we have value {value}")