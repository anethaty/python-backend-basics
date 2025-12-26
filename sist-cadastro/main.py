import app

while True:
    print('\n-- Sistema de Biblioteca --\n')
    print('\n 1. Adicionar Livro\n')
    print('\n 2. Listar Livros\n')
    print('\n 3. Sair\n')

    opcao = app.opcao()

    if opcao == 1:
        app.func_principal()
        print('Livro cadastrado com sucesso!')
    elif opcao == 2:
        app.listar_dados()
    elif opcao == 3:
        print('Programa encerrado!')
        break
    else:
        print('Opção inválida. Tente novamente...')