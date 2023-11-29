# This is first exercise
# Find the repeating elements in a list

mylist = [1, 2, 3, 4, 12, 45, 1, 2, 54, 65, 77, 8, 1, 2,]
myset = set({})

maxln = len(mylist)

for x in range(0, maxln, 1):
    for i in range(x+1, maxln, 1):
        if mylist[x] == mylist[i]:
            myset.add((mylist[x]))

print("De duplicated elements are: ", myset)


# End of the first exercise


