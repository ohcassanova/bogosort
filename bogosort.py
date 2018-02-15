import random

listsize = int(input("How big do you want the list to be? "))
numlist =[]

for x in range(listsize):
    num = random.randint(1, 100)
    numlist.append(num)

def bogosort(listtosort): 
    count = 0
    while not all(b >= a for a, b in zip(listtosort, listtosort[1:])):
        random.shuffle(listtosort)
        print(listtosort)
        count += 1
    print("Wow! That only took {0} steps to sort!".format(count))
    return listtosort

bogosort(numlist)
