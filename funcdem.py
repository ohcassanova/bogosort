import random

listsize = int(input("How big do you want the list to be? "))
numlist =[]

for x in range(listsize):
    num = random.randint(1, 100)
    numlist.append(num)

def checklistsorted(list):
    for x in range(len(list)):
        if list[x] < list[x + 1]:
            pass


def bogosort(numlist): #This can't be used to check is a list is sorted
    if sorted(numlist) == numlist:
        return numlist
    else:
        numlist = random.shuffle(numlist)
        print(numlist)
        bogosort(numlist)

print(bogosort(numlist))
