from time import sleep

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo *= -1

    if inicio < fim:
        while inicio <= fim:
            print(inicio, end=" -> ", flush=True)
            sleep(0.5)
            inicio += passo
        print("FIM")

    elif inicio > fim:
        while inicio >= fim:
            print(inicio, end=" -> ", flush=True)
            sleep(0.5)
            inicio -= passo
        print("FIM")

    else:
        print(f"{inicio} -> FIM")

print("=" * 50)
print("Contagem de 1 até 10 puiando 1 casa...")
sleep(1)
contador(1, 10, 1)
print("=" * 50)
print("Contagem de 10 até 0 diminuindo 2 casas...")
sleep(1)
contador(10, 0, 2)
print("=" * 50)
print("Contador personalizado...")
contador(
    int(input("Ínicio: ")),
    int(input("Fim: ")),
    int(input("Passo: "))
)
print("=" * 50)