def removeArrayFromArray(array1):
    print(array1)
    array1.pop(0)
    print(array1)
    return array1


array1 = [1,2,3,4,5,6,7]

array3 = removeArrayFromArray(array1)
print(array3)