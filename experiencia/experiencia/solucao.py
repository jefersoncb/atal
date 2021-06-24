''' função que seleciona a melhor experiência '''
def melhor_experiencia(L,C):
    melhoresExperiencias =[]
    for i in range(len(C)):
        total = 0
        experiencia = 0
        pratos = ""
        controle = []


        for j in range(i,len(C)):
            if total <= L:
               dados = C[j]
               if (total + dados[1]) > L :
                   continue

               else:
                   pratos+=dados[0]+","
                   total += dados[1]
                   experiencia+=dados[2]
            controle.append(pratos + " " + str(experiencia))
        melhoresExperiencias.append(controle)

    exp = melhoresExperiencias[0][0].split(" ")

    for i in range(len(melhoresExperiencias)):
        for j in range(len(melhoresExperiencias[i])):
            lista_pos = melhoresExperiencias[i][j].split(" ")
            if int(lista_pos[1]) > int(exp[1]):
                exp = lista_pos
    return  exp[0].split(",")



nome=[("Caviar", 100, 20), ("Pizza", 20, 5), ("Bode", 11, 10), ("Lagosta", 90, 15)]


print(melhor_experiencia(120,nome))