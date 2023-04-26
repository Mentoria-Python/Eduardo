'''
Crie um dicionário d e coloque nele os dados fornecidos pelo usuário:
nome, idade, telefone, endereço.
Também usando d, imprima todos os itens do cicionário no formato chave:
valor, ordenado pela chave.
'''


class Pessoa:
    def __init__(self, nome: str, idade: int, telefone: str, endereco: str):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.endereco = endereco


class ListaDePessoas:
    def __init__(self):
        self.pessoas = []

    def adicionar_pessoa(self, pessoa):
        self.pessoas.append(pessoa)

    def apresentar_pessoas(self):
        for pessoa in self.pessoas:
            print('Nome: ', pessoa.nome)
            print('Idade: ', pessoa.idade)
            print('Telefone: ', pessoa.telefone)
            print('Endereco: ', pessoa.endereco)
            print()


lista_de_pessoas = ListaDePessoas()
numero_pessoas = int(input('Digite quantas pessoas deseja inserir: '))

for i in range(numero_pessoas):
    print(f'{i+1} pessoa:')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    telefone = input('Telefone: ')
    endereco = input('Endereco: ')
    pessoa = Pessoa(nome, idade, telefone, endereco)
    lista_de_pessoas.adicionar_pessoa(pessoa)

print('As pessoas inseridas foram:')
lista_de_pessoas.apresentar_pessoas()
