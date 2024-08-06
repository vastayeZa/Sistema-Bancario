class Banco:
    def __init__(self):
        self.saldo = 0.0
        self.transacoes = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.transacoes.append(f"Depósito: +R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido!")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.transacoes.append(f"Saque: -R${valor:.2f}")
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        elif valor > self.saldo:
            print("Saldo insuficiente para saque!")
        else:
            print("Valor de saque inválido!")

    def exibir_extrato(self):
        print("\nExtrato:")
        if self.transacoes:
            for transacao in self.transacoes:
                print(transacao)
        else:
            print("Nenhuma transação realizada.")
        print(f"Saldo atual: R${self.saldo:.2f}\n")

def main():
    banco = Banco()

    while True:
        print("Bem-vindo ao Banco!")
        print("Selecione uma operação:")
        print("1. Depósito")
        print("2. Saque")
        print("3. Extrato")
        print("4. Sair")

        opcao = input("Digite a opção desejada (1-4): ")

        if opcao == '1':
            valor = float(input("Digite o valor do depósito: "))
            banco.depositar(valor)
        elif opcao == '2':
            valor = float(input("Digite o valor do saque: "))
            banco.sacar(valor)
        elif opcao == '3':
            banco.exibir_extrato()
        elif opcao == '4':
            print("Obrigado por usar o Banco. Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
