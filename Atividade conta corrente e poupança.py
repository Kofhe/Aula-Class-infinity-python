#faça uma classe pai chamada Conta
#nela vai ter as caracteristicas: numero_conta, titular, saldo(não é recebido pelo usuário)

#2classes filhas
#conta corrente e conta poupança

#saldo não é recebido pelo usuario
from datetime import datetime
print(datetime.now().time())

class Conta:
    def __init__(self,numero_conta,titular):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = 0 #não quero que o usuario passe na hora de criar o objeto
        self.data_criacao=datetime.strftime(datetime.now().date(),"%d/%m/%Y")#marca o momento de criação desta entidade

#classe corrente
class Corrente(Conta):
    def __init__(self, numero_conta, titular):
        super().__init__(numero_conta, titular)
        self.cheque_especial=100
        self.credito=400

    def sacar(self,valor_saque):
        # retirar o valor do saldo
        if self.saldo < valor_saque:
            print("Saldo insuficiente!")
            if self.saldo + self.cheque_especial < valor_saque:
                print("Cheque especial não cobre")
            else:
                self.saldo -= valor_saque
                print("Saque efetuado com sucesso! Cheque especial utilizado")

                return ""
        pass
    
    def depositar(self,valor_deposito):
        # adicionar o valor no saldo
        self.saldo +=valor_deposito
        pass

    def transferir(self,conta_destinada:Conta,valor):
        # decrementa de uma conta e adiciona na outra 
        if self.salo < valor:
            print("Saldo insuficiente para transferência")
            return ""
        self.saldo -= valor
        conta_destinada.saldo += valor
        print("Transferência efetuada com sucesso!")
        pass

#classe poupança
class Poupança(Conta):
    def __init__(self, numero_conta, titular):
        super().__init__(numero_conta, titular)
        self.rendimento=6

    def gerar_juros(self):
        # gera um juros de 1% sobre o saldo
        self.saldo += (1/100)*self.saldo
        pass    

cliente1 = Corrente(numero_conta="0123",titular="Sei la")
cliente2 = Corrente(numero_conta="0001",titular="Batatinha")

print("O valor do saldo da conta 1 éigual a",cliente1.saldo)
print("O valor do saldo da conta 1 éigual a",cliente2.saldo)


print(cliente2.saldo)
conta1.transferir(conta_destinada=cliente2,valor=20)
print(cliente1.saldo)   
print(cliente2.saldo)   

contapou=Poupança(numero_conta="6789",titular="Batata")
contapou.saldo = 100
print(contapou.saldo)   
contapou.gerar_juros()
print(contapou.saldo) 
