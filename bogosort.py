import random

listsize = int(input("How big do you want the list to be? "))
numlist =[]

for x in range(listsize):
    num = random.randint(1, 100)
    numlist.append(num)



def bogosort(listtosort): #This can't be used to check if a list is sorted
    if all(b >= a for a, b in zip(listtosort, listtosort[1:])):
        return listtosort
    else:
        random.shuffle(listtosort)
        print(listtosort)
        bogosort(listtosort)

bogosort(numlist)
