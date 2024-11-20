import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}' .format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Tempo completo' )

while True:

    t = input ('Digite os segundos: ')

    if not t.isdigit() or int(t) <= 0:
        print("Por favor, insira um número válido maior que 0")
        continue

    countdown(int(t))

    a= input ("Deseja recomeçar [s/n]:  ").strip().lower()

    if a == "s":
        pass
    elif a == "n":
        print("Encerrando programa...")
        break
    else:
        print("Opção Inválidade! Encerrando Programa...")
        break   

input()