array = [-1,1,-2,2,3]

min = 3
for i in range(len(array)):
    if array[i]<0:continue
    else:
        if array[i]>0 and array[i]<array[min]:
            min = i

print(min)