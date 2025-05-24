def q1():

    ano = int(input("Digite o ano: "))
    periodo = int(input("Digite o periodo: "))

    for i in range(1, 5):
        print(ano + periodo * i, end=" ")

def q2():
  
  while True:
    n = int(input("Digite um número inteiro (ou -1 para sair): "))
    if n == -1:
        break

    if n < 2:
        print("Não")
    else:
        primo = True
        for i in range(2, n):
            if n % i == 0:
                primo = False
                break
        if primo:
            print("Primo")
        else:
            print("Não")

def q3():

    soma = 0
    cont = 0

    while True:
        valor = float(input("Digite um valor: ").replace(',', '.'))
        if valor < 0:
            break
        soma += valor
        cont += 1

    if cont > 0:
        media = soma / cont
        print(f"{soma:.2f}".replace('.', ','))
        print(f"{media:.2f}".replace('.', ','))


def q4():

    dias = int(input("Digite a quantidade de dias: "))
    km = int(input("Digite a quantidade de km: "))

    if dias == 0:
        print("Valor inválido")
    else:
        preco = 90 * dias
        limite = 100 * dias
        if km > limite:
            extra = km - limite
            preco += extra * 12
        print(f"{preco:.2f}".replace('.', ','))

def q5():

    escala = input("Digite a escala (C/F/K): ").strip().upper()
    temp = float(input("Digite a temperatura: ").replace(',', '.'))

    if escala == "C":
        if temp < -273.15:
            print("Valor de temperatura abaixo do mínimo")
        else:
            f = temp * 1.8 + 32
            k = temp + 273.15
            print(f"{f:.2f} °F".replace('.', ','))
            print(f"{k:.2f} mil".replace('.', ','))

    elif escala == "F":
        if temp < -459.67:
            print("Valor de temperatura abaixo do mínimo")
        else:
            c = (temp - 32) / 1.8
            k = (temp + 459.67) / 1.8
            print(f"{c:.2f} °C".replace('.', ','))
            print(f"{k:.2f} mil".replace('.', ','))

    elif escala == "K":
        if temp < 0:
            print("Valor de temperatura abaixo do mínimo")
        else:
            c = temp - 273.15
            f = temp * 1.8 - 459.67
            print(f"{c:.2f} °C".replace('.', ','))
            print(f"{f:.2f} °F".replace('.', ','))
    else:
        print("Escala inválida")

if __name__=="__main__":
    q5() 