menu = """ 

[0] Depositar
[1] Sacar
[2] Extrato
[9] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0 
LIMITE_SAQUES= 3


while True:
    opçao = input(menu)

    if opçao == "0":
        print("Deposíto")
        valor = float(input("Digite o valor do Deposíto: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"

    elif opçao == "1":
        print("Saque")
        if saldo != 0:
            saque = float(input("Digite a quantidade a ser sacada: "))
            if saque <= limite:
                if numero_saques < LIMITE_SAQUES :
                    if saldo > saque:
                        if valor > 0:
                            saldo -= saque
                            extrato += f"Saque: R$ {saque:.2f}\n"
                    else:
                        print("Não Possui saldo disponivel para saque no momento.")
                else:
                    print("Quantidades de saques excedida.")
            else:
                print("Valor informado maior do que o permitido, saque maximo: 500.00")
    elif opçao == "2":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    elif opçao == "9":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
