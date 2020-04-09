# Linguagem de Programação II
# Atividade Contínua 02 - Classes e Herança
#
# e-mail: debora.santos@aluno.faculdadeimpacta.com.br





class Reptil:
    """
    Classe mãe - não deve ser editada
    """
    def __init__(self, nome, cor, idade):
        self.nome = nome
        self.cor = cor
        self.idade = idade

    def tomar_sol(self):
        return '{} tomando sol'.format(self.nome)

    def botar_ovo(self):
        if self.idade > 2:
            return '{} botou um ovo'.format(self.nome)
        else:
            return '{} ainda não atingiu maturidade sexual'.format(self.nome)


class Mamifero:
    """
    Classe mãe - não deve ser editada
    """
    def __init__(self, nome, cor_pelo, idade, tipo_pata):
        self.nome = nome
        self.cor_pelo = cor_pelo
        self.idade = idade
        self.tipo_pata = tipo_pata

    def correr(self):
        return '{} correndo'.format(self.nome)

    def mamar(self):
        if self.idade <= 1:
            return '{} mamando'.format(self.nome)
        else:
            return '{} já desmamou'.format(self.nome)


class Camaleao(Reptil):
    """
    Exemplo de solução do exercício:

    Além dos atributos da classe mãe, possui o atributo:
    inseto_favorito, do tipo string.

    Implementa os métodos específicos:
    mudar_de_cor() e comer_inseto()
    """
    def __init__(self, nome, cor, idade, inseto_favorito):
        super().__init__(nome, cor, idade)
        self.inseto_favorito = inseto_favorito

    def mudar_de_cor(self):
        return '{} mudando de cor'.format(self.nome)

    def comer_inseto(self):
        return '{} comendo inseto'.format(self.nome)


class Cavalo(Mamifero):
    
    def __init__(self, nome, cor_pelo, idade, tipo_pata, cor_crina):
        super().__init__(nome, cor_pelo, idade, tipo_pata)
        self.cor_crina = cor_crina

    def galopar (self):
        return '{} galopando'.format(self.nome)

    def relinchar (self):
        return '{} relinchando'.format(self.nome)


class Cobra(Reptil):
    
    def __init__(self, nome, cor, idade, veneno):
        super().__init__(nome, cor, idade)
        self.veneno = veneno
        if veneno == True:
            print('Venenosa')
        else:
             print('Não venenosa')

    def rastejar (self):
        return '{} rastejando'.format(self.nome)

    def trocar_pele (self):
        return '{} trocando de pele'.format(self.nome)



class Cachorro(Mamifero):
    
    def __init__(self, nome, cor_pelo, idade, tipo_pata, raca):
     super().__init__(nome, cor_pelo, idade, tipo_pata)
     self.raca = raca

    def latir (self):
        return '{} latindo'.format(self.nome)

    def rosnar (self):
        return '{} rosnando'.format(self.nome)




class Jacare(Reptil):
    
    def __init__(self, nome, cor,idade, num_dentes):
        super().__init__(nome, cor, idade)
        self.num_dentes = num_dentes

    def atacar(self):
        return '{} atacando'.format(self.nome)

    def dormir(self):
        return '{} dormindo'.format(self.nome)



class Gato(Mamifero):
    
    def __init__(self, nome, cor_pelo, idade, tipo_pata, vidas):
        super().__init__(nome, cor_pelo, idade, tipo_pata)
        self.vidas = 7

    def miar(self):
        return '{} miando'.format(self.nome)

    def gato_morreu(self):
        while self.vidas > 0:
            self.vidas = self.vidas - 1
            print("Gato morreu. Gato tem {} vidas".format(self.vidas))
        print("Gato não tem mais vidas")
        

def main():
    Cavalo1 = Cavalo('Pangaré', 'Caramelo', 11, 'Normal', 'Azul')
    print(Cavalo1.relinchar())
    print(Cavalo1.galopar())

    Cobra1 = Cobra('Morgana', 'Preto', 19, True)
    print(Cobra1.rastejar())
    print(Cobra1.trocar_pele())

    Cachorro1 = Cachorro('Nina', 'Branco e Mel', 3,'Normal', 'Shitzu')
    print(Cachorro1.latir())
    print(Cachorro1.rosnar())

    Jacare1 = Jacare('Manolo', 'Verde', 15, 40)
    print(Jacare1.atacar())
    print(Jacare1.dormir())

    Gato1 = Gato('Alaska', 'Branco', 12, 'Normal', 5)
    print(Gato1.miar())
    print(Gato1.gato_morreu())

if __name__ == "__main__":
    main ()