def q1():
    ano = int(input(""))
    pulo = int(input(""))
    for i in range(ano+ pulo, (ano + (pulo*4)) + 1 , pulo):
        print(i, end=" ")

def q2():
    ler_numeros = True
    while ler_numeros:
        n = int(input(""))
        if n == -1:
            ler_numeros = False
            break
        primo = True
        for i in range(n-1, 1, -1):
            if n % i == 0:
                primo = False
        if primo:
            print("Primo")
        else:
            print("Não")
                

def q3():
    pass

def q4():
    pass