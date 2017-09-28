import random
import math
def mergeSort(mylist1, mylist2, mylist3):
    if len(mylist1) > 1:
        mid = len(mylist1) // 2
        lefthalf1 = mylist1[:mid]
        righthalf1 = mylist1[mid:]
        lefthalf2 = mylist2[:mid]
        righthalf2 = mylist2[mid:]
        lefthalf3 = mylist3[:mid]
        righthalf3 = mylist3[mid:]

        mergeSort(lefthalf1, lefthalf2, lefthalf3)
        mergeSort(righthalf1, righthalf2, righthalf3)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf1) and j < len(righthalf1):
            if lefthalf1[i] < righthalf1[j]:
                mylist1[k] = lefthalf1[i]
                mylist2[k] = lefthalf2[i]
                mylist3[k] = lefthalf3[i]
                i = i + 1
            else:
                mylist1[k] = righthalf1[j]
                mylist2[k] = righthalf2[j]
                mylist3[k] = righthalf3[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf1):
            mylist1[k] = lefthalf1[i]
            mylist2[k] = lefthalf2[i]
            mylist3[k] = lefthalf3[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf1):
            mylist1[k] = righthalf1[j]
            mylist2[k] = righthalf2[j]
            mylist3[k] = righthalf3[j]
            j = j + 1
            k = k + 1
count = int(input("Enter the number of points:"))
maxvalue = 100
minvalue = 0
pt = list()
x = list()
y = list()
for i in range(count):
    pt.append(i + 1)
    x.append(random.randint(minvalue, maxvalue))
    y.append(random.randint(minvalue, maxvalue))

print("INITIALLY:\n",pt)
print(x)
print(y)

mergeSort(x, y, pt)

print("SORTED LIST:\n",pt)
print(x)
print(y)
