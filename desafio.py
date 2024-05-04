"""
Modificar o código para funções de sacar, depositar e extrato. 
Crias duas novas funções cadastrar cliente, e conta bancaria e vincular ao cliente(Usuário)
Argumentos parametros saque > ** keyword only, saldo,valor,extrato,limite,numeros_saques,limite_saques, retornar saldo e extrato. 
Argumentos * posicional deposito > saldo,valor,extrato, retorno saldo e extrato
Extrato deve receber argumentos por posição e nome *saldo,**extrato
Criar usuário gravar em uma lista composta por nome,data de nascimento,cpf,endereço. O endereço é uma string com formato: Logradouro,nro - bairro - cidade/sigla estado.
Deve gravar somente os números do cpf e não pode cadastrar 2 usuário com msm cpf. 

Cria conta Corrente, armazenar em uma lista composta por agencia numero da conta e usuário o número da conta é sequencial iniciando em 1.
O número da agencia é fixo em 0001. POde ter mais de uma conta mas uma conta pertence a somente um usuário. 
Dica: Para vincular um usário a conta filtre a lista de usuários buscando o número do cpf informado para cada usuário da lista. 
"""
import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    [0] Depositar
    [1] Sacar
    [2] Extrato
    [3] Novo Usuário
    [4] Nova conta
    [5] Listar Contas
    [9] Sair
    => """
    return input(textwrap.dedent(menu))
def sacar(*,saldo, valor, extrato, limite, numero_saques,limite_saques):
    saldo_excedido = valor > saldo
    limite_excedido = valor > limite
    saques_excedidos = numero_saques >= limite_saques

    if saldo_excedido:
        print("Operação não realizada! sem saldo no momento. ")

    elif limite_excedido:
        print("Operação não realizada! O valor do saque foi maior que o permitido.")
    
    elif saques_excedidos:
        print("Operação não realizada! O número máximo de saques atingido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação não realizada!, Valor informado é invalido.")
    return saldo, extrato

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito: R$ {valor:.2f}\n"
        print("Deposito realizado !")
    else:
        print("Operação não realizada, Valor informado inválido.")
    return saldo, extrato

def consultar_extrato(saldo, /, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\tR$ {saldo:.2f}\n")
    print("==========================================")

def filtro_usuários(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def novo_usuario(usuarios):
    cpf = input("Informe o cpf (somente números): ")
    usuario = filtro_usuários(cpf,usuarios)
    if usuario:
        print("Usuário ja cadastrado !")
        return
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe da data de nascimento com dia/mes/ano: ")
    endereco = input("Digite o endereço com (Lagradouro, nro - bairo - cidade/UF): ")
    usuarios.append({"nome":nome, "data_nascimento":data_nascimento, "cpf":cpf,"endereco":endereco})

    print("Usuárico cadastrado !! ")

def cria_conta(agencia, conta, usuarios):
    cpf = input("Informe o cpf do usuário: ")
    usuario = filtro_usuários(cpf, usuarios)
    if usuario:
        print("Conta cadastrada com sucesso!")
        return {"agencia":agencia, "numero_conta":conta,"usuario":usuario}
    print("Usuário não encontrado !!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência:\t{conta['agencia']}
            C-C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def codigo_principal():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0 
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "0":
            valor = float(input("Informe o valor do deposito: "))

            saldo, extrato = deposito(saldo,valor,extrato)

        elif opcao == "1":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

        elif opcao == "2":
            consultar_extrato(saldo,extrato=extrato)

        elif opcao == "4":
            numero_conta = len(contas)+1
            conta = cria_conta(AGENCIA,numero_conta,usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "3":
            novo_usuario(usuarios)
        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "9":
            break
        else:
            print("Operação invalida !!")

codigo_principal()