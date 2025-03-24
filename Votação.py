def votaçao():
    from collections import Counter
    from pickletools import decimalnl_short
    candidatos = {

    }
    while True:
        decisao = input(
            "gostaria de adicionar um nome para votaçao? (coloque [s] para sim e [n] para nao) ")
        if decisao == 'n':
            break
        else:
            nome = input("Digite o nome do candidato: ")
            numero = input("Numero dele: ")

        if candidatos.get(nome):
            print("Ja existe o aluno ", nome)
        else:
            candidatos[numero] = nome
    print(candidatos)

    votos = Counter()
    while True:
        voto = input('Digite o número do candidato (ou "fim" para encerrar): ')
        if voto == 'fim':
            break  # sai do while True
        if voto in candidatos:  # se é um dos números de candidato válido
            votos.update([voto])
        else:
            print(f'Número inválido: {voto}')

    print('Resultado:')
    for numero, qtd_votos in votos.most_common():
        print(f'{candidatos[numero]} teve {qtd_votos} votos')
votaçao()