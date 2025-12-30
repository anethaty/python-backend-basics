import json

def carregar_arquivo():
    try: 
        with open('data.json', 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return[]
    
def salvar_arquivo(lista_atualizada):
    with open('data.json', 'w', encoding='utf-8') as arquivo:
        json.dump(lista_atualizada, arquivo, indent=4)


def coletar_dados():
    livraria = {}
    nome = input(f"\nDigite o nome do livro: ")
    autor = input(f"\nDigite o autor do livro: ")
    ano = int(input(f"\nDigite o ano de lançamento do livro: "))
    preco = float(input(f"\nDigite o preço do livro: "))

    livraria['nome'] = nome
    livraria['autor'] = autor
    livraria['ano'] = ano
    livraria['preco'] = preco
    
    return livraria 

def opcao():
    return int(input('Digite a opção desejada: '))


def func_principal():
    dict_dados = coletar_dados()

    dados_atuais = carregar_arquivo()
    dados_atuais.append(dict_dados)
    salvar_arquivo(dados_atuais)

def listar_dados():
    lista = carregar_arquivo()
    
    if lista == None:
        print('Não há livros cadastrados.') 

    for livro in lista:
        for inf, dado in livro.items():
            print(f'| {inf} : {dado} |', end="")
        print()


