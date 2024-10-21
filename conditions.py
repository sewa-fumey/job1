
def job1():
    valeur1 = int(input("entre un nombre entre 0 et 20 "))
    valeur2 = int(input("entre un second nombre entre 0 et 20 ")) 

    if valeur1 == valeur2:
        print("valeur1 est egal à valeur2 ")
    else:
        print("les deux valeurs ne sont pas égales ")
    

def job2():
    A = 18 
    B = int(input("quel age as tu ? "))
    if B >= A:
        print("tu peux voter ")
    else:
        print("tu ne peux pas voter ")


def job3():
    for N in range (101):
       if N != 26 and N != 37 and N != 88:
            print(N)


def job4():
    for N in range (1,101):
        if N % 3 == 0 and N % 5 == 0:
            print("FizzBuzz")
        elif N % 3 == 0:
            print("FIzz")
        elif N % 5 == 0:
            print("Buzz")
        else:
            print(N)


def job5():
    for N in range (2,1001):
            if N % 2 == 0 and N != 2:
                continue
            if N % 3 == 0 and N != 3:
                continue 
            print (N)   
"""
nombre = 0
boolean = True
while nombre < 1001:
    for j in range(2, nombre - 1):
        if nombre % j == 0:
            boolean = False
            break
    if boolean == True:
        print(nombre)
    nombre = nombre + 1
    boolean = True

"""        
# print('toto')


def job_5():
    for N in range(2,1001):
        for x in range(2,N):
            if N % x == 0:
                break
        else:
            print(N)


job_5()


def job6():
    X = int(input("entrez un nombre : "))
    if X % 2 == 0:
        print(f"le nombre {X} est pair ")
    else:
        print(f"le nombre {X} est impair ")


def job7():
    chaine = "abcdefghijklmnopqrstuvwxyz " 
    for N in range(1,len(chaine) + 1,2):
        print(chaine[:N])


