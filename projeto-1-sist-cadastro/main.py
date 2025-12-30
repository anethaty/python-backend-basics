import app

while True:
    print('\n\n-- Sistema de Biblioteca --')
    print('\n 1. Adicionar Livro')
    print('\n 2. Listar Livros')
    print('\n 3. Buscar Dados do Livro')
    print('\n 4. Editar Livro')
    print('\n 5. Excluir Livro')
    print('\n 6. Sair')
    print('-- --------------------- --\n')

    opcao = app.opcao()

    if opcao == 1:
        app.adicionar_livro()
        print('Livro cadastrado com sucesso!')
    elif opcao == 2:
        app.listar_dados()
    elif opcao == 3:
        app.buscar_dados()
    elif opcao == 4:
        app.editar_dados()
    elif opcao == 5:
        app.excluir_livro()
    elif opcao == 6:
        print('\nPrograma encerrado!')
        break
    else:
        print('Opção inválida. Tente novamente...')