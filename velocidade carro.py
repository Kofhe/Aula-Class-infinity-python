class Carro:
    def __init__(self,modelo,ano,cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0
    
    def acelerar(self):
        self.acelerar +=8
        return self.velocidade
    
    def frear(self):
        self.frear -3
        return self.frear
    
carro1 = Carro(modelo = "Palio",ano = 2008,cor = "Vermelho")
print(carro1.modelo)

print(carro1.velocidade)
carro1.acelerar()
carro1.frear()
print(carro1.velocidade)
