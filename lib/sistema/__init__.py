def linha(tam=42):
    return '-' * tam


def cabecalho(texto):
    print(linha())
    print(texto.center(len(linha())))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    for pos, c in enumerate(lista):
        print(f'{pos + 1} - {c}')
    print(linha())
    opcao = leiaInt('Sua Opção: ')
    return opcao


def leiaInt(txt):
    """
    -> Função que valida se o input é inteiro.
    :param txt: mensagem para ser exibida no input;
    :return: retorna o número;
    Feito por Kaique Teixeira dos Anjos nas aulas do Curso Em Vídeo
    """
    while True:
        try:
            num = int(input(f'{txt}'))
        except (ValueError, TypeError):
            print('ERRO! Digite um número inteiro válido!')
            continue
        else:
            return num

