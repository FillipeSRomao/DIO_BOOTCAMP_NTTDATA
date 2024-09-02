menu = """
Selecione uma opção abaixo:
[depositar]
[saque]
[transferir]
[extrato]
[sair]

=> """

saldo = 0
limite = 500
transferir = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "depositar":
        valor = float(input("Informe o valor do depósito: "))

        if valor >= 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'

        else: print("Operação falhou! O valor informado é invaálido.")

    elif opcao == "saque":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque execede o limite.")

        elif excedeu_saque:
            print("Operação falhou! Número máximo de saques excedido")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "transferir":
        valor = float(input("Informe o valor para tranferência: "))

        sem_saldo = valor > saldo

        if sem_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif valor >= saldo:
            saldo -= valor
            extrato += f"Tranferido: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "extrato":
        print("\n ========== EXTRATO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==============================")

    elif opcao == "sair":
        break

else:
    print("Operação inválida, por favor, selecione novamente a operação desejada.")

