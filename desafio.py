from CONSTANTES import *
import random 

def formatarInteiro(numero):
    tamNum = len(numero)
    if (len(numero) > 0):
        palavraEspecial = ""
        if (tamNum <= 9 and tamNum > 6):
            palavraEspecial =  " milhões"
        elif(tamNum <= 6 and tamNum > 3):
            palavraEspecial = " mil"
        else: 
            palavraEspecial = ""

        if (tamNum == 9 or tamNum == 6 or tamNum == 3):
            if (numero[0] == "1"):
                if (numero[0:2] == "100"):
                    numeroPorExtenso = ""
                    numeroPorExtenso += dictCentenasEspeciais[numero[0:3]] + " " + palavraEspecial
                    return numeroPorExtenso + formatarInteiro(numero[3:])
                elif (numero[0] == "0"):
                    return "" + palavraEspecial
                else: 
                    numeroPorExtenso = ""
                    numeroPorExtenso += dictCentenasEspeciais[numero[0]] + " e "
                    return numeroPorExtenso + formatarInteiro(numero[1:])
            else:
                if (numero[1:2] == "00"):
                    numeroPorExtenso = ""
                    numeroPorExtenso += dictCentenas[numero[0]] + palavraEspecial
                    return numeroPorExtenso + formatarInteiro(numero[3:])
                else: 
                    numeroPorExtenso = ""
                    numeroPorExtenso += dictCentenas[numero[0]] + " e "
                    return numeroPorExtenso + formatarInteiro(numero[1:])

        elif (tamNum == 2 or tamNum == 5 or tamNum == 8): 
            if (numero[0] == "1"):
                numeroPorExtenso = ""
                numeroPorExtenso += dictDezenasEspeciais[numero[0:2]] + " " + palavraEspecial
                return numeroPorExtenso + formatarInteiro(numero[2:]) 
            else:
                if (numero[1] == "0"):
                    numeroPorExtenso = ""
                    numeroPorExtenso += dictDezenas[numero[0]] + " " + palavraEspecial
                    return numeroPorExtenso + formatarInteiro(numero[2:])
                else:
                    numeroPorExtenso = ""
                    numeroPorExtenso += dictDezenas[numero[0]] + " e "
                    return numeroPorExtenso + formatarInteiro(numero[1:])
        elif (tamNum == 1 or tamNum == 4 or tamNum == 7): 
            numeroPorExtenso = ""
            numeroPorExtenso += dictUnidade[numero[0]] + str(palavraEspecial +" e " if tamNum != 1 else " ")
            return numeroPorExtenso + formatarInteiro(numero[1:]) 
    else: 
        return "reais"

def formatCentavos(numero):
    tamNumero = len(numero)
    if(tamNumero == 2):
        if (numero[0] == "1"):
            return " e " + dictDezenasEspeciais[numero[0:2]] + " centavos"
        else: 
            if(numero[0] != "0"):
                return " e " + dictDezenas[numero[0]] +" e " +formatCentavos(numero[1:])
            else:
                return "" + formatCentavos(numero[1:])

    else: 
        return " e "+ dictUnidade[numero[0]] + " centavos"

def __main__():
    dadosNumerosArquivo = open("dados.txt", "a")
    print("Inicio...")
    for i in range(1,999999999,1000):
        dadosNumerosArquivo.write(str(i+1)+","+str(random.randint(0,99))+"\n")

    dadosNumerosArquivo.close()

    print("Por extenso..")
    dadosNumeros = open("dados.txt", "r")
    dadosPorExtensoArquivo = open("dadosExtenso.txt", "a")
        
    for numero in dadosNumeros:
        numeroInteiro = numero[0]
        numeroDecimal = numero[1]
        text = numeroInteiro == "1" and "um real" or formatarInteiro(numeroInteiro)
        text += formatCentavos(numero)

        dadosPorExtensoArquivo.write( str(numero)+ " =>" + str(text)+"\n")

    dadosPorExtensoArquivo.close()
    
    dadosNumeros.close()
    print("Finalizou")

__main__()




