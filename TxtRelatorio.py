import datetime

agora = datetime.datetime.now()

'''
with open("Vendas","w") as vendas:
    vendas.write("camisa,2,50.00\n")
    vendas.write("calca,4,55.00\n")
    vendas.write("moletom,3,40.00\n")
    vendas.write("tenis,1,130.00\n")
                                    
'''

with open("Vendas","r") as vendas:
    
    linhas = vendas.readlines()

valoresFinais = []

for linha in linhas:
    itens_organizado = linha.strip().split(",")
    
    # Coleta os dados de cada item
    produto = itens_organizado[0]
    quantidade = int(itens_organizado[1])
    preco = float(itens_organizado[2])
    
    # Calcula o valor total
    valorFinal = quantidade * preco
    
    

    # Cria a string formatada e imprime
    print(f"{quantidade} {produto}(s) a {preco} cada, total: {valorFinal}")
    
    # Adiciona o valor final na lista
    valoresFinais.append(valorFinal)

    
    print("Valor Final:", valorFinal)
    print("Valores Finais até agora:", valoresFinais)

with open("Relatorios de Vendas.", "w") as relatorios:
    for linha in linhas:
        itens_organizado = linha.strip().split(",")
        produto = itens_organizado[0]
        quantidade = int(itens_organizado[1])
        preco = float(itens_organizado[2])
        valorFinal = quantidade * preco

        # Escreve a linha formatada no relatório
        relatorios.write(f"{quantidade} {produto}(s) a {preco} cada, total: {valorFinal}\n")

    # Escreve o total geral
    relatorios.write(f"\nTOTAL GERAL: {sum(valoresFinais)}\n")
    relatorios.write(f"HORARIO DO RELATORIO: {agora.strftime('%d/%m/%Y %H:%M')}")

