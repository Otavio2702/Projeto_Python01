import os

restaurantes = [
    {"nome": "Pizza hut", "categoria": "Italiana", "ativo": False},
    {"nome": "Hamburguer", "categoria": "Americana", "ativo": True},
    {"nome": "Lá mexicana", "categoria": "Mexicana", "ativo": True},
]


def exibir_nome_do_programa():
    print("Sabor express")


def exibir_opcoes():
    """Exíbi as opções para o usuário"""
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Alternar restaurante")
    print("4. Sair\n")


def escolher_opcao():
    """Onde o usuário escolhe a opção desejada, e o programa executa a ação correspondente"""
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def finalizar_app():
    """vai limpar a tela e finalizar o app caso o usuário escolha a opção 4"""
    os.system("cls")
    print("Finalizando o app")


def exibir_subtitulo(texto):
    """Essa função exíbi o subtitulo em outras funções"""
    os.system("cls")
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_novo_restaurante():
    """Essa função cadastra um novo restaurante

    inputs:
    - Nome do restaurante que deseja cadatras
    - Categoria do restaurante cadastrado

    outputs:
    - Adiciona um novo restaurante a lista de restaurante

    """
    os.system("cls")
    exibir_subtitulo("Cadastro de restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o nome da categoria do restaurante {nome_restaurante}:")
    dados_do_restaurante = {
        "nome": nome_restaurante,
        "categoria": categoria,
        "ativo": False,
    }
    restaurantes.append(dados_do_restaurante)
    print(f"restaurante {nome_restaurante} foi cadastrado com sucesso!\n")
    voltar_ao_menu_principal()


def listar_restaurantes():
    """essa função lista os restaurantes"""
    os.system("cls")
    exibir_subtitulo("Lista de restaurantes")

    print(f"{'Nome do restaurante'.ljust(21)} | {'Categoria'.ljust(20)} | {'Status'}")
    print()
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "Ativado" if restaurante["ativo"] else "Destivado"
        print(f".{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")
    voltar_ao_menu_principal()


def alternar_estado_do_restaurante():
    """Essa função altera o estado do restaurante

    input:
    - nome do restaurante que deseja mudar o estado

    outputs:
    - Se o restaurante Digitado estiver na lista do dicionárioo estado dele muda
    - Se o restaurante digitado não estiver na lista do dicionário, exíbi que ele não foi encontrado

    """
    exibir_subtitulo("Alternando estado do restaurante")
    nome_restaurante = input(
        "Digite o nome do restaurante que deseja alterar o estado: "
    )
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = (
                f"O restaurante {nome_restaurante} foi ativado com sucesso"
                if restaurante["ativo"]
                else f"O restaurante {nome_restaurante} foi desativado com sucesso"
            )
            print(mensagem)
    if not restaurante_encontrado:
        print("O restaurante não foi encontrado")

    voltar_ao_menu_principal()


def opcao_invalida():
    """Essa função será exibida caso o usuário digite uma tecla fora das opções"""
    print("Opção inválida!\n")
    voltar_ao_menu_principal()


def voltar_ao_menu_principal():
    input("\nPressione uma tecla para voltar ao menu principal")
    main()


def main():
    """Função principal que inicia o programa"""
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == "__main__":
    main()
