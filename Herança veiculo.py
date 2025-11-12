class Veiculo:
    def __init__(self,mddelo,ano,cor):
        self.modelo=modelo 
        self.ano=ano 
        self.cor=cor

#classe carro que herda veículo

class Carro(Veiculo):
    def __init__(self, mddelo, ano, cor):
        super().__init__(mddelo, ano, cor)

#classe moto que herda de veiculo
class Moto(Veiculo):
    def __init__(self, mddelo, ano, cor):
        super().__init__(mddelo, ano, cor)
