publico = False

while publico == False:
    publico_maximo = input("Defina o público máximo do evento: ")

    if publico_maximo.isdigit():
        publico_maximo = int(publico_maximo)
        publico = True
    else:
        print("Entrada incorreta.")

pessoas_inscritas = 0
adultos = jovens = universitarios = criancas = 0
orcamento = 0
encerramento = False
cod_encerramento = "admbreak123"
print(f"Cod.Encerramento -> {cod_encerramento}\n\n")


while not encerramento:
    print("\n|Menu de Opções|\
           \n1-Inscrição\
           \n2-Encerrar Programa\n")
    opcao = input("Insira qual das opções deseja realizar: ")

    if opcao.isdigit():
        opcao = int(opcao)
        match opcao:
            case 1:
                if pessoas_inscritas < publico_maximo:
                    print("\n|CATEGORIAS|\
                        \n1-Adultos - R$40,00\
                        \n2-Jovens de 10 a 17 anos - R$15,00\
                        \n3-Universitários - R$20,00\
                        \n4-Crianças até 9 anos - Isentos de pagamento\n\
                        \n\n|INSCRIÇÃO|\n")
                    opcao_inscricao = input("Insira qual das categorias o participante se enquadra na inscrição: ")

                    if opcao_inscricao.isdigit():
                        opcao_inscricao = int(opcao_inscricao)

                        cliente_crianca = False

                        match opcao_inscricao:
                            case 1:
                                adultos += 1
                                cobrado = 40
                                print("Categoria: Adulto")
                            case 2:
                                jovens += 1
                                cobrado = 15
                                print("Categoria: Jovem")
                            case 3:
                                tentativas = 0
                                universitario = False
                                while tentativas < 2 and universitario == False:
                                    matricula = input("Matrícula do Universitário [9 dígitos]: ")

                                    if matricula.isdigit() and len(matricula) == 9:
                                        universitarios += 1
                                        universitario = True
                                        print("Categoria: Universitário")
                                        cobrado = 20
                                    elif tentativas < 2:
                                        print("Matrícula inválida. Tente mais uma vez.")
                                        tentativas +=1

                                if universitario == False:
                                    adultos += 1
                                    print("Limite de tentativas atingido: 2. Redirecionando para..\n Categoria: Adulto")
                                    cobrado = 40
                            case 4:
                                criancas += 1
                                print("Categoria: Criança")
                                cliente_crianca = True
                            case _:
                                print("Opção inválida.")

                        if opcao_inscricao in (1, 2, 3, 4):
                            tentativas = 0
                            pagamento = False

                            if cliente_crianca == False:
                                while pagamento == False:
                                    validez = False
                                    while validez == False:
                                        recebimento = input("Valor recebido pelo participante: ")
                                        validez = True
                                        for c in recebimento:
                                            if c not in("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."):
                                                validez = False

                                        if validez == False:
                                                print("Entrada incorreta.")

                                    recebimento = float(recebimento)
                                    if recebimento > cobrado:
                                        print(f"Troco: R${recebimento - cobrado:.2f}")
                                        pagamento = True
                                    elif recebimento < cobrado:
                                        print(f"Pagamento insuficiente.")
                                        tentativas += 1
                                    else:
                                        pagamento = True

                                print("Pagamento finalizado. Entrada permitida.")
                                orcamento += cobrado
                            else:
                                print("Criança isenta de pagamento. Entrada permitida.")
                        
                    else:
                        print("Categoria Inválida. Voltando para menu inicial")
                else:
                    print("Máximo de pessoas atingido.")
            case 2:
                insert_cod_encerramento = input("Insira o código de encerramento do sistema: ")
                if insert_cod_encerramento == cod_encerramento:
                    encerramento = True
                else:
                    print("Código inválido.")
            case _:
                print("Opção inválida.")
    else:
        print("Entrada incorreta.")


    pessoas_inscritas = adultos + jovens + universitarios + criancas
if orcamento <= 300:
    premio = orcamento * 0.1
elif orcamento > 300 and orcamento <= 700:
    premio = orcamento * 0.15
elif orcamento < 700:
    premio = orcamento * 0.2

primeiro = premio * 0.5
segundo = premio * 0.3
terceiro = premio * 0.2

if adultos*40 > jovens*15 and adultos*40 > universitarios*20:
    maiscontribuiu = "Adultos"
elif jovens*15 > adultos*40 and jovens*15 > universitarios*20:
    maiscontribuiu = "Jovens"
elif universitarios*20 > adultos*40 and universitarios*20 > jovens*15:
    maiscontribuiu = "Universitários"

if adultos*40 < jovens*15 and adultos*40 < universitarios*20:
    menoscontribuiu = "Adultos"
elif jovens*15 < adultos*40 and jovens*15 < universitarios*20:
    menoscontribuiu = "Jovens"
elif universitarios*20 < adultos*40 and universitarios*20 < jovens*15:
    menoscontribuiu = "Universitários"

print(f"|ESTATÍSTICAS|\
    \n\nPúblico total: {pessoas_inscritas};\
    \nArrecadação - Adultos: R${adultos * 40.00};\
    \nArrecadação - Jovens: R${jovens * 15.00};\
    \nArrecadação - Universitários com matrícula: R${universitarios * 20.00};\
    \nValor total arrecadado: R${orcamento};\n\
    \
    \n\nCategoria pagante que mais arrecadou: {maiscontribuiu};\
    \nCategoria pagante que menos arrecadou: {menoscontribuiu};\
    \
    \n\nTicket médio - Somente pagamentes: R${orcamento/pessoas_inscritas};\
    \nTicket médio - Geral: R${orcamento/(pessoas_inscritas-criancas)};\
    \
    \n\nVagas restantes: {publico_maximo - pessoas_inscritas};\
    \
    \n\nPrêmio Total: R${premio};\
    \nPremiação Individual:\n 1ºLugar:R${primeiro};\n 2ºLugar:R${segundo};\n3ºLugar:{terceiro};")
    