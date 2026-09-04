# Declaração de autoria
# Nome: Marcus Vinícius Leite dos Santos
# Declaro que este código foi desenvolvido por mim, com base no meu próprio
# entendimento e esforço. Não houve plágio ou cópia integral de terceiros.
# Ferramentas de IA, quando utilizadas, foram apenas como apoio ao aprendizado
# e não para a geração integral deste código.

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
cod_encerramento = "5020jzp"
print(f"Cod.Encerramento -> {cod_encerramento}\n\n")


while not encerramento:
    print(f"\n|Menu de Opções|\
           \n1-Inscrição\
           \n2-Encerrar Programa\
        \n\nVagas restantes: {publico_maximo-pessoas_inscritas}\n")
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

                        'CATEGORIZAÇÃO'
                        match opcao_inscricao:
                            case 1:
                                categoria = "adulto"
                                cobrado = 40
                                print("Categoria: Adulto")
                            case 2:
                                categoria = "jovem"
                                cobrado = 15
                                print("Categoria: Jovem")
                            case 3:
                                universitario = False

                                matricula = input("Matrícula do Universitário [9 dígitos]: ")

                                if matricula.isdigit() and len(matricula) == 9:
                                    categoria = "universitario"
                                    universitario = True
                                    print("Categoria: Universitário")
                                    cobrado = 20

                                if universitario == False:
                                    categoria = "adulto"
                                    print("Matrícula inválida ou ausente. Redirecionando para..\n Categoria: Adulto")
                                    cobrado = 40
                            case 4:
                                criancas += 1
                                print("Categoria: Criança")
                                cliente_crianca = True
                            case _:
                                print("Opção inválida.")


                        'ETAPA DE PAGAMENTO'
                        if opcao_inscricao in (1, 2, 3, 4):
                            pagamento = False

                            if cliente_crianca == False:
                                encerrar_pagamento = False
                                while pagamento == False and encerrar_pagamento == False:
                                    validez = False
                                    while validez == False:
                                        recebimento = input("Valor recebido pelo participante: ")
                                        validez = True
                                        for c in recebimento:
                                            if c not in("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", ",") or recebimento[0] in (".", ","):
                                                
                                            #Se a entrada digitada:
                                            #não tiver números ou vírgula/ponto decimal 
                                            #ou for iniciada por virgula/ponto decimal
                                            #dará erro, portanto será inválida
                                                validez = False
                                        if recebimento == "":
                                            #Se a entrada digitada:
                                            #for vazia
                                            #dará erro, portanto será inválida
                                            validez = False

                                        if validez == False:
                                                print("Entrada incorreta.")

                                    recebimento = recebimento.replace(",", ".")
                                    recebimento = float(recebimento)
                                    if recebimento > cobrado:
                                        print(f"Troco: R${recebimento - cobrado:.2f}")
                                        pagamento = True
                                    elif recebimento < cobrado:
                                        print(f"Pagamento insuficiente. R${cobrado-recebimento:.2f} para completar")
                                        opcao_completar = ""
                                        while opcao_completar.lower() not in("completar","cancelar"):
                                            opcao_completar = input("Deseja completar o valor ou cancelar o pagamento: ")
                                            if opcao_completar.lower() == "completar":
                                                orcamento += recebimento
                                                cobrado -= recebimento
                                            elif opcao_completar.lower() == "cancelar":
                                                encerrar_pagamento = True
                                            else:
                                                print("Entrada incorreta.")
                                    else:
                                        pagamento = True
                                if pagamento == True:
                                    print("Pagamento finalizado. Entrada permitida.")
                                    match categoria:
                                        case "adulto":
                                            adultos +=1
                                        case "jovem":
                                            jovens+=1
                                        case "universitario":
                                            universitarios+=1
                                    orcamento += cobrado
                                else:
                                    print("Retornando ao menu")
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
elif orcamento > 700:
    premio = orcamento * 0.2

primeiro = premio * 0.5
segundo = premio * 0.3
terceiro = premio * 0.2

print(pessoas_inscritas, criancas)
if pessoas_inscritas != criancas:
    #DEFINIÇÃO DE QUEM CONTRIBUIU MAIS  
    if adultos*40 > jovens*15 and adultos*40 > universitarios*20:
        maiscontribuiu = "Adultos"
    elif jovens*15 > adultos*40 and jovens*15 > universitarios*20:
        maiscontribuiu = "Jovens"
    elif universitarios*20 > adultos*40 and universitarios*20 > jovens*15:
        maiscontribuiu = "Universitários"
    elif adultos*40 == jovens*15 and adultos*40 > universitarios*20:
        maiscontribuiu = "Adultos e Jovens - Empatados"
    elif adultos*40 == universitarios*20 and adultos*40 > jovens*15:
        maiscontribuiu = "Adultos e Universitários - Empatados"
    elif jovens*15 == universitarios*20 and jovens*15 > adultos*40:
        maiscontribuiu = "Jovens e Universitários - Empatados"
    elif jovens*15 == universitarios*20 and jovens*15 == adultos*40:
        maiscontribuiu = "Adultos, Jovens e Universitários - Empatados"



    #DEFINIÇÃO DE QUEM CONTRIBUIU MENOS
    if adultos*40 < jovens*15 and adultos*40 < universitarios*20:
        menoscontribuiu = "Adultos"
    elif jovens*15 < adultos*40 and jovens*15 < universitarios*20:
        menoscontribuiu = "Jovens"
    elif universitarios*20 < adultos*40 and universitarios*20 < jovens*15:
        menoscontribuiu = "Universitários"
    elif adultos*40 == jovens*15 and adultos*40 < universitarios*20:
        menoscontribuiu = "Adultos e Jovens - Empatados"
    elif adultos*40 == universitarios*20 and adultos*40 < jovens*15:
        menoscontribuiu = "Adultos e Universitários - Empatados"
    elif jovens*15 == universitarios*20 and jovens*15 < adultos*40:
        menoscontribuiu = "Jovens e Universitários - Empatados"
    elif jovens*15 == universitarios*20 and jovens*15 == adultos*40:
        menoscontribuiu = "Adultos, Jovens e Universitários - Empatados"
        
else:
    menoscontribuiu = maiscontribuiu = "Público Zero - Nenhuma das Categorias"


print(f"|ESTATÍSTICAS|\
    \n\nPúblico total: {pessoas_inscritas};\
      \nVagas restantes: {publico_maximo - pessoas_inscritas};")

if pessoas_inscritas > 0:
    print(f"\n\nTicket médio - Geral: R${orcamento/pessoas_inscritas:.2f};")

    if pessoas_inscritas != criancas and criancas>0:
        print(f"\nTicket médio - Exceto crianças: R${orcamento/(pessoas_inscritas-criancas)};")
        
    print(f"\nVagas restantes: {publico_maximo - pessoas_inscritas};")


print(f"\nArrecadação - Adultos: R${adultos * 40.00:.2f};\
    \nArrecadação - Jovens: R${jovens * 15.00:.2f};\
    \nArrecadação - Universitários com matrícula: R${universitarios * 20.00:.2f};\
    \nValor total arrecadado: R${orcamento:.2f};\
    \
    \n\nCategoria pagante que mais arrecadou: {maiscontribuiu};\
    \nCategoria pagante que menos arrecadou: {menoscontribuiu};\
    \
    \n\nPrêmio Total: R${premio:.2f};\
    \nPremiação Individual:\n 1ºLugar:R${primeiro:.2f};\n 2ºLugar:R${segundo:.2f};\n3ºLugar:R${terceiro:.2f};")
    
