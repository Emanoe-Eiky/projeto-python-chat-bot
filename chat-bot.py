'''from time import sleep
while True:
    oi = input("Oi? ")
    if oi == "oi":
        bem = input("Tudo bem? ")
        if bem in "SIM estou claro ".upper() or bem == "Estou indo".upper() or bem == "estou bem".upper():
            print("OK")

        nome = input("Qual seu nome? ")
        sleep(1)
        print("O meu é jissele")
        sleep(1)
        if nome == "deivid":
            print("belo nome")
        break
    else: print("?",sep=" ") #sep é para pular um alinha



while True:
    bem = input(f"Olá {nome}, Tudo bem? ").title()
    if bem == "sim".title():
        print("legal")
        break
    elif bem == "nao".title():
        print("Espero que fique bem!")
        break
    else: print("\033[1;31mnão estou programado para responder isso!!!\033[m tente sim ou nao,",sep=" ")

dialogo = input("")'''
from time import  sleep
while True:
    def idad():
        per = input("Qual é a sua idade? :")


    print("Olá")
    num = input("Tudo bem?: ")
    if num in "SIM sim ":
        print("ok")
        per = input("Qual é a sua idade? :")

    elif num in "Nao nao":
        print("Espero ue fique bem")
        com = input("quer convesar :")
        if com in "nao": break
        idad()


    else:
        print("\033[1;31mnao estou programado para responder isso\033[m")
