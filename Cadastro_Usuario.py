class Usuario:
    def __init__(self, nome, email, numero):
        self.nome = nome
        self.email = email
        self.numero = numero

    def exibirDados(self):
        print(f"Dados do Cliente: Nome: {self.nome}, Email: {self.email}, Número: {self.numero}\n")

# Lista para armazenar os clientes
clientes = []

# Menu interativo
while True:
    print("1 - Cadastrar cliente")
    print("2 - Listar todos os clientes")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do cliente: ")
        email = input("Digite o email do cliente: ")
        numero = input("Digite o número do cliente: ")

        novo_cliente = Usuario(nome, email, numero)
        clientes.append(novo_cliente)
        print("Cliente cadastrado com sucesso!\n")

    elif opcao == "2":
        if not clientes:
            print("Nenhum cliente cadastrado ainda.\n")
        else:
            for cliente in clientes:
                cliente.exibirDados()

    elif opcao == "3":
        print("Saindo do sistema. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.\n")