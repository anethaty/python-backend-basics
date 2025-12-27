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


def adicionar_livro():
    dict_dados = coletar_dados()

    dados_atuais = carregar_arquivo()
    dados_atuais.append(dict_dados)
    salvar_arquivo(dados_atuais)

def listar_dados():
    lista = carregar_arquivo()
    
    if lista == None:
        print('Não há livros cadastrados.') 

    for livro in lista:
        for k, v in livro.items():
            print(f'| {k} : {v} |', end="")
        print()

def buscar_dados():
    inf_livro = input('Qual livro deseja buscar a informação? ')
    inf_busca = input('Qual informação que deseja buscar?\n A. Autor\n B. Ano\n C. Preço\n\n')

    if inf_busca.upper() == 'A':
        inf_busca = 'autor'
    elif inf_busca.upper() == 'B':
        inf_busca = 'ano'
    elif inf_busca.upper() == 'C':
        inf_busca = 'preco'
    else:
        print(f'\nseleção inválida')
        buscar_dados()

    lista = carregar_arquivo()
    if lista == None:
        print(f'\nNão há livros cadastrados')
    
    for livro in lista:
        if livro['nome'] == inf_livro:
            print(f'\n{livro['nome']} : {livro[inf_busca]}')
            return
        
    print(f'\nO livro {inf_livro} não foi cadastrado!')


def editar_dados():
    edit_livro = input('Qual livro deseja editar? ')
    inf_edit = input('Qual informação que deseja editar?\n A. Autor\n B. Ano\n C. Preço\n\n')
    dado_novo = input('Digite a nova informação: ')

    #passa para inteiro ou float se necessário
    if inf_edit.upper() == 'B':
        dado_novo = int(dado_novo)
    if inf_edit.upper() == 'C':
        dado_novo = float(dado_novo)

    if inf_edit.upper() == 'A':
        inf_edit = 'autor'
    elif inf_edit.upper() == 'B':
        inf_edit = 'ano'
    elif inf_edit.upper() == 'C':
        inf_edit = 'preco'
    else:
        print(f'\nseleção inválida')
        editar_dados()

    lista = carregar_arquivo()
    if lista == None:
        print(f'\nNão há livros cadastrados')

    for livro in lista:
        if livro['nome'] == edit_livro:
            livro[inf_edit] = dado_novo

            salvar_arquivo(lista)

    print(f'O livro {edit_livro} não foi cadastrado!!')
    

def excluir_livro():
    exc_livro = input('Qual livro deseja excluir? ')

    lista = carregar_arquivo()
    if lista == None:
        print(f'\nNão há livros cadastrados')

    for livro in lista:
        if livro['nome'] == exc_livro:
            lista.remove(livro)

            salvar_arquivo(lista)
            print(f'\nLivro {exc_livro} excluso com sucesso!')

    print(f'Livro {exc_livro} não está cadastrado!')
    
