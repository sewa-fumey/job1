
def job1():
    fruits = ["pomme","cerise","orange"]
    print(fruits)



def job2():
    fruits = ["pomme", "cerise","orange"]
    print(fruits[1])


def job3():
    fruits = ["pomme","cerise","orange"]
    fruits.append("melon")
    print(fruits) 


def job4():
    fruits = ["pomme","cerise","orange","melon"]
    fruits.insert(2, "mangue")
    print(fruits)



def job5():
    L = [1,2,3,4,5]
    print(L)
    print(L[1])
    L[3] = L[2] + L[4]
    print(L)
    print(L[-1])


def job_5():
    L = list(range(1,6)) # permet de lister les nombres
    print(L)
    print(L[1])
    L[3] = L[2] + L[4]
    print(L)
    print(L[-1])


def job6():
    L = list(range(1,6))
    print(L)
    L[0], L[-1] = L[-1], L[0]
    print (L)


def job13():
    L = [10,20,30,20,10,50,60,40,80,50,40]
    print(L)
    L = [x for i, x in enumerate(L) if x not in L[:i]]
    print(L) 


