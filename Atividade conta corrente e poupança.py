#faça uma classe pai chamada Conta
#nela vai ter as caracteristicas: numero_conta, titular, saldo(não é recebido pelo usuário)

#2classes filhas
#conta corrente e conta poupança

#saldo não é recebido pelo usuario
from datetime import datetime

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

cliente1 = Corrente(numero_conta="0123",titular="Sei la")
print(cliente1.saldo)

#classe poupança
class Poupança(Conta):
    def __init__(self, numero_conta, titular):
        super().__init__(numero_conta, titular)
        self.rendimento=6

cliente2=Poupança(numero_conta="6789",titular="Batata")
print(cliente2.data_criacao)
