itens = [['1- Alface americano','2- Alface crespa','3- Alho poró','4- Capim santo','5- Cebola','6- Cebolinha','7- Coentro','8- Couve folha','9- Chinguezay (acelga chinesa)','10- Espinafre','11- Hortelã','12- Salsinha','13- Rúcula'],['1- Banana pacovan (unidade)','2- Cana(saquinho)','3- Laranja comum (4 Unidades)','4- Laranja mimo (4 Unidades)','5- Maracujá (kg)'],['1- Batata doce (kg)','2- Cará (kg)','3- Cenoura(molho)','4- Jerimum (kg)','5- Macaxeira (kg)','6- Rabanete(molho)','7- Quiabo (15 Un)'],['1- Fava seca (Kg)','2- Mel italiana (250 g)','3- Mel italiana (500 g)','4- Mel no favo (450 g)','5- Ovos de capoeira (un)','6- Polpa de cajá (400g)','7- Própolis (20 ml)','8- Pão sem trigo (grande)','9- Pão com trigo (grande)','10- Pão com trigo (pequeno)','11- Bolo(sem trigo)','12- Bolinho de bacia(c/trigo)','13- Mini pizza (un)','14- Pizza brotinho','15- Bolacha com trigo (saquinho)','16- Sucos sem açucar (200 ml)','17- Sucos com açucar (200 ml)','18- Sucos com ou sem açucar (1 l)','19- Refeições congeladas (500 g)','20- Refeições congeladas (750 g)','21-Hambúrguer de ora-pro-nóbis, (6 Un)','22- Molhos prontos','23- Massa artesanal lasanha ou taglatelle'],['1- Pepita de girassol','2- Homus de grão de bico com paprika','3- Bisnaga Maionese de pepita de girassol (250 ml)','4- Pimentas ao mel de engenho','5- Confit de tomatinho, pimenta, pimentão ou berinjela','6- Geleia de tomate com pimenta/abacaxi/manga','7- Capotana Siciliana'],['1- Quiche de macaxeira c/ alho poró','2- Quiche de macaxeira c/ tomate seco','3- Sanduíche sem glúten de ricota','4- Sanduíche sem glúten de caponata Siciliana','5- Sanduíche sem glúten de ragu'],['1- Empada de falso camarão','2- Empada de antepasto de berinjela','3- Empada de tofu com cebola caramelizada','4- Pãozinhos de inhames recheados']]
precos = [[2.50,2.50,2.00,2.50,3.00,2.50,2.50,2.50,3.00,3.00,2.50,2.50,2.50],[0.25,2.00,2.00,7.00,2.00],[4.00,5.00,3.00,5.00,4.00,2.50,2.00],[12.00,20.00,35.00,25.00,1.00,6.00,16.00,13.00,13.00,7.00,10.00,2.00,3.00,5.00,5.00,3.00,3.00,10.00,12.00,15.00,12.00,10.00,12.00],[5.00,5.00,10.00,15.00,15.00,13.00,13.00],[5.00,5.00,6.00,6.00,6.00],[5.00,5.00,5.00,5.00]]
setores = ['1- folhas e hortaliças  o molho','2- frutas','3- raízes, tubérculos, legumes e afins','4- outros','5- Pastinhas, antepastos e geleias','6- Lanches (sem trigo)','7- Lanches (com trigo)']
carrinho = list()
quantidade = list()
total = 0
notafiscal = str()
g = 0

print(" ")
print('**************************************************')
print(" ")
print('                  BEM VINDO(A)')
print(" ")
print('ESCOLHA UM SETOR PARA COMEÇAR A FAZER SUAS COMPRAS')
print(" ")
print('**************************************************')
op = 1
while op != 0 :
    print("Setores")
    print(" ")
    print("0- Sair")
    for i in range(0,len(setores)) :
        print(setores[i])
    print("8- Finalizar Compra")

    print(" ")
    op = int(input("Insira Número do Setor: "))
    print(" ")
    if op != 0 and op < 8 :
        i = op -1
        for j in range(0,len(precos[i])) :
            print(itens[i][j],precos[i][j])
        
        opcao = 1
        while opcao != 0 :
            print(" ")
            opcao = int(input("Nº do Iten ou Digite 0 para Voltar: "))
            print(" ")
            h = opcao -1
            if opcao != 0 :
                quantidade = (int(input("Insira a Quantidade do Produto: ")))
                print(" ")
                carrinho.append(f'{itens[i][h]:<25}{precos[i][h]:<7}{quantidade:<5}{precos[i][h]*quantidade}\n')
                total += precos[i][h]*quantidade
                g += 1
                print("Total do Carrinho: ",total)

    elif op != 0 and op == 8 :
        print(" ")
        nome = str(input('Insira Nome do Cliente: '))
        print(" ")
        endereco = str(input("Insira Endereço do Cliente: "))
        print(" ")
        pagamento = str(input("Insira Forma de Pagamento (Dinheiro),(Débito) ou (Crédito): "))
        op = 0

notafiscal += str("-----------------------------------------\n")
notafiscal += str("---------------nota fiscal---------------\n")
notafiscal += str("-----------------------------------------\n")
notafiscal += str(f'Nome                   Preço  Qnt  Total\n')

for i in carrinho:
    notafiscal += i
notafiscal += str("-----------------------------------------\n")
notafiscal += str(f'total a ser pago{total:>30}\n\n')
notafiscal += str(f'Nome: {nome}\n')
notafiscal += str(f'Endereço: {endereco}\n')
notafiscal += str(f'Pagamento: {pagamento}\n')
print(notafiscal)   

arquivo = open(f'{nome}notafiscal.txt', "x+", encoding= 'utf8')
arquivo.write(notafiscal)