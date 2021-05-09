from CONSTANTES import *

def formatarInteiro(numero, init = False):
    tamNum = len(numero)
    if (len(numero) > 0):
        palavraEspecial = ""
        if (tamNum <= 9 and tamNum > 6):
            palavraEspecial =  " milhões"
        elif(tamNum <= 6 and tamNum > 3):
            palavraEspecial = " mil"
        else: 
            palavraEspecial = " "

        if(numero[0] == "0"):
            if (tamNum == 1):
                return " " + formatarInteiro(numero[1:])
            else:
                return formatarInteiro(numero[1:])


        if (tamNum == 9 or tamNum == 6 or tamNum == 3):
            if (numero[0] == "1"):
                if (numero[0:3] == "100"):
                    numeroPorExtenso = ""
                    numeroPorExtenso += dictCentenasEspeciais[numero[0:3]] + palavraEspecial
                    return numeroPorExtenso + formatarInteiro(numero[3:])
                elif (numero[0] == "0"):
                    return "" + palavraEspecial
                else: 
                    numeroPorExtenso = ""
                    numeroPorExtenso += dictCentenasEspeciais[numero[0]] + " e "
                    return numeroPorExtenso + formatarInteiro(numero[1:])
            else:
                if (numero[1:3] == "00"):
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
                numeroPorExtenso += dictDezenasEspeciais[numero[0:2]] +  palavraEspecial
                return numeroPorExtenso + formatarInteiro(numero[2:]) 
            else:
                if (numero[1] == "0"):
                    numeroPorExtenso = ""
                    numeroPorExtenso += dictDezenas[numero[0]] + palavraEspecial
                    return numeroPorExtenso + formatarInteiro(numero[2:])
                else:
                    numeroPorExtenso = ""
                    numeroPorExtenso += dictDezenas[numero[0]] + " e "
                    return numeroPorExtenso + formatarInteiro(numero[1:])
        elif (tamNum == 1 or tamNum == 4 or tamNum == 7): 
            numeroPorExtenso = ""
            if (numero[0] == "1" and palavraEspecial == " milhões" and init):
            #     palavraEspecial = " milhão"
                numeroPorExtenso += dictUnidade[numero[0]] + str(palavraEspecial + (" e " if tamNum != 1 and numero[1:7] != "000000" else ""))
            elif(numero[0] == "1" and palavraEspecial == " mil" and init):
                numeroPorExtenso += str(palavraEspecial + (" e " if (tamNum != 1) and numero[1:4] != "000" else ""))
            else: 
                numeroPorExtenso += dictUnidade[numero[0]] + str(palavraEspecial + (" e " if (tamNum != 1) else ""))
            return numeroPorExtenso + formatarInteiro(numero[1:]) 
    else: 
        return " reais"

def formatCentavos(numero):
    tamNumero = len(numero)
    if(numero == "00"):
        return ""

    elif(tamNumero == 2):
        if (numero[0] == "1"):
            return " e " + dictDezenasEspeciais[numero[0:2]] + " centavos"
        else: 
            if(numero[0] != "0"):
                return " e " + dictDezenas[numero[0]] + formatCentavos(numero[1:])
            else:
                return "" + formatCentavos(numero[1:])

    else: 
        return " e "+ dictUnidade[numero[0]] + " centavos"

def __main__():
    dadosNumerosArquivo = open("dados.txt", "r")
    dadosPorExtensoArquivo = open("dadosPorExtenso.txt", "w") 
        
    for numero in dadosNumerosArquivo:
        try:
            numero = numero.split("\n")
            numeroWrite = numero[0]

            try:
                numero = numero[0].split(",")
                numeroInteiro = numero[0]
                numeroDecimal = numero[1]
                int(numeroInteiro)
                int(numeroDecimal)
            except:
                raise Exception("Erro, os dados inseridos não são números.")
                

            if (len(numeroInteiro) > 9 or len(numeroDecimal) > 2):
                raise Exception("Erro, não é possível realizar a conversão, o tamanho do número não contemplado pelo algorítimo.")

            text = numeroInteiro == "1" and "um real" or formatarInteiro(numeroInteiro, True)
            text = text.replace("  ", " ")
            text += formatCentavos(numeroDecimal)

            dadosPorExtensoArquivo.write(str(numeroWrite)+ " =>" + str(text)+"\n")

        except Exception as err:
            dadosPorExtensoArquivo.write(str(numeroWrite)+ " =>" + str(err.args)+"\n")

    dadosPorExtensoArquivo.close()
    dadosNumerosArquivo.close()

__main__()




